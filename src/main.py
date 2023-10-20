from datetime import datetime

import schedule

import crawler

# https://www.e-cadeiras.com.br/cadeiras/cadeiras-de-escritorio
# https://www.flexform.com.br/cadeiras/cadeiras-de-escritorio

def job():
    print("\n Execute job. Time: {}".format(str(datetime.now())))
    crawler.execute(5)

crawler = crawler.Crawler() # Cria uma objeto da classe Crawler.
schedule.every(1).minutes.do(job)
#crawler.execute(5)
while True:
    schedule.run_pending()
