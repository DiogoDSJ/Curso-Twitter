import requests
from bs4 import BeautifulSoup

class Crawler:

    def requestData(self, url: str):
        content = requests.get(url)
        site = BeautifulSoup(content.text, 'html.parser')
        return site

    def extractFromFlexform(self):
        siteFlexform = self.requestData("https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio")
        productname = siteFlexform.find_all('a', attrs={'class' : 'produto__title'})
        productprice = siteFlexform.find_all('p', attrs={'class' : 'produto__price'})
        return productname, productprice

    def toString(self, productname: str, productprice: float):
        tamanho1 = len(productname)
        tamanho2 = len(productprice)
        a = 0
        while (tamanho1 != 0 or tamanho2 != 0):
            print(productname[a].text.strip())
            print(productprice[a].text.strip())
            a += 1
            tamanho1 -= 1
            tamanho2 -= 1

    def extractFromECadeiras(self):
        siteECadeiras = self.requestData("https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio")
        productname = siteECadeiras.find_all('h3', attrs={'class' : 'product-name'})
        productprice = siteECadeiras.find_all('span', attrs={'class' : 'price-best'})
        return productname, productprice

