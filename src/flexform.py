import requests
from bs4 import BeautifulSoup

# https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio
# https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio

scrap = requests.get("https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio", "html.parse")

content = scrap.content
site = BeautifulSoup(content, 'html.parser')
productname = site.find_all('a', attrs={'class' : 'produto__title'})
productprice = site.find_all('p', attrs={'class' : 'produto__price'})


tamanho1 = len(productname)
tamanho2 = len(productprice)

a = 0
while(tamanho1 != 0 or tamanho2 != 0):
    print(productname[a].text.strip())
    print(productprice[a].text)
    a += 1
    tamanho1 -= 1
    tamanho2 -= 1