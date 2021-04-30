from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import telegram
import logging

url = ['https://br.investing.com/currencies/usd-brl', 'https://br.investing.com/indices/bovespa']

req = Request(url[0], headers={'User-Agent': 'Mozilla/5.0'})
web = urlopen(req).read()
bs = BeautifulSoup(web, 'lxml')
dolar = bs.select('.pid-2103-pcp')[0].get_text()

req = Request(url[1], headers={'User-Agent': 'Mozilla/5.0'})
web = urlopen(req).read()
bs = BeautifulSoup(web, 'lxml')
bovespa = bs.select('.pid-17920-pcp')[0].get_text()

#objeto principal
bot = telegram.Bot('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

bot.send_message(chat_id=xxxxxxxxxx, text=f'Dolar  {dolar}')
bot.send_message(chat_id=xxxxxxxxxxx, text=f'Bovespa  {bovespa}')

#log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)











