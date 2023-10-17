from datetime import datetime
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from database import Database


class Crawler:

    def __init__(self):
        load_dotenv()
        self.db = Database()

    def requestData(self, url: str): # Extrai dados de um determinado site.
        content = requests.get(url)
        site = BeautifulSoup(content.text, 'html.parser')
        return site

    def extractFromFlexform(self): # Extrai o nome e o valor das cadeiras do site da flexform.
        siteFlexform = self.requestData(os.getenv("FLEXFORM") + f'/cadeiras/cadeiras-de-escritorio?_offset=0&_limit=96&_sort=&')
        products = siteFlexform.find_all('article', attrs={'class' : 'produto'})
        for product in products:
            productname = product.find('a', attrs={'class' : 'produto__title'}).text.strip()
            productprice = product.find('p', attrs={'class' : 'produto__price'}).text.strip()
            productimage = product.find('img', attrs={'class' : 'img-fluid'}).get('src').strip()
            productlink = product.find('a', attrs={'class' : 'produto__title'}).get('href').strip()
            offer = {"title": productname, "price": productprice, "image": productimage, "link": productlink , "date" : datetime.now()} # put in db
            response = self.db.insert(offer)
            if response is not None: # Se o produto não existe, ou seu preço foi atualizado.
                print("Oferta foi adicionada/atualizada.")
            else: # Produto não teve valor alterado.
                print("Produto não teve seu valor alterado.")


    def extractFromECadeiras(self, pages: int = 1): # Extrai o nome e o valor das cadeiras do site da E-Cadeiras.
        page = 1
        while(page <= pages):
            siteECadeiras = self.requestData(os.getenv("ECADEIRAS") + f"/buscapagina?fq=C%3a%2f6331%2f6334%2f&PS=40&sl=fc437e63-3393-44cb-a1db-d941aacb6990&cc=4&sm=0&PageNumber={page}")
            products = siteECadeiras.find_all('li', attrs={'layout' : 'fc437e63-3393-44cb-a1db-d941aacb6990'})
            for product in products:
                productname = product.find('h3', attrs={'class' : 'product-name'}).text.strip()
                productprice = product.find('span', attrs={'class' : 'price-best'}).text.strip()
                productimage = product.find('figure', attrs={'class' : 'product-image'}).img.get('src')
                productlink = product.find('h3', attrs={'class' : 'product-name'}).a.get('href')
                offer = {"title": productname, "price": productprice, "image": productimage, "link": productlink , "date" : datetime.now()} # put in db
                response = self.db.insert(offer)
                if response is not None: # Se o produto não existe, ou seu preço foi atualizado.
                    print("Oferta foi adicionada/atualizada.")
                else: # produto não teve valor alterado.
                    print("Produto não teve seu valor alterado.")
            page+=1
