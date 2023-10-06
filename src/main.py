import requests
from bs4 import BeautifulSoup
import crawler

# https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio
# https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio



crawler = crawler.Crawler()
flexformlabel = crawler.extractFromFlexform()
ecadeiraslabel = crawler.extractFromECadeiras()
print("Tabela E-Cadeiras:\n")
crawler.toString(ecadeiraslabel[0], ecadeiraslabel[1])
print("\nTabela Flexform:\n")
crawler.toString(flexformlabel[0], flexformlabel[1])
