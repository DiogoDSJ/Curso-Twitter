import requests
from bs4 import BeautifulSoup
import crawler

# https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio
# https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio



crawler = crawler.Crawler() # Cria uma objeto da classe Crawler.
flexformlabel = crawler.extractFromFlexform() # Extrai dados da Flexform.
ecadeiraslabel = crawler.extractFromECadeiras() # Extrai dados da E-Cadeiras.
# Abaixo é printado os dados de maneira organizada.
print("Tabela E-Cadeiras:\n")
crawler.toString(ecadeiraslabel[0], ecadeiraslabel[1])
print("\nTabela Flexform:\n")
crawler.toString(flexformlabel[0], flexformlabel[1])
