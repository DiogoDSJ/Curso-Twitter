import crawler

# https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio
# https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio


string = "Lite"
crawler = crawler.Crawler() # Cria uma objeto da classe Crawler.
crawler.extractFromFlexform()
crawler.extractFromECadeiras(5)
print(crawler.db.search(string))
