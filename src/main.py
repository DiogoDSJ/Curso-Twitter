import requests
from bs4 import BeautifulSoup

# https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio
# https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio

scrap = requests.get("https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio", "html.parse")

content =  scrap.content
site = BeautifulSoup(content, 'html.parser')
productname = site.find_all('h3', attrs={'class' : 'product-name'})
productprice = site.find_all('span', attrs={'class' : 'price-best'})

tamanho1 = len(productname)
tamanho2 = len(productprice)

a = 0
while(tamanho1 != 0 or tamanho2 != 0):
    print(productname[a].text)
    print(productprice[a].text)
    a += 1
    tamanho1 -= 1
    tamanho2 -= 1
