import requests
from bs4 import BeautifulSoup
import lxml
import json

currency='usd'
sel_buy='sell'
exchanger='exchanger'
city='all'
url=f'https://minfin.com.ua/currency/auction/{exchanger}/{currency}/{sel_buy}/{city}'
req=requests.get(url).text
soup=BeautifulSoup(req, 'lxml')
for k in range(len(soup.find_all('script'))):
    try:
        if soup.find_all('script')[k]['type']=="application/json":
            js_currency=json.loads(soup.find_all('script')[k].text)
    except:
        pass
js=js_currency['props']['initialState']['operations']['operations']
def spec():
    for k in range(len(js)):
        try:
            print(js[k]['address'])
            print(js[k]['rate']['currency'])
            print('BUY:',js[k]['rate']['buy']['value'])
            print('SELL:',js[k]['rate']['sell']['value'])
            print('----------------------------------------')
            
        except:
            print('something went wrong')
def all():
    for k in range(len(js_currency['props']['initialState']['operations']['operations'])):
        print('sell or buy:',js_currency['props']['initialState']['operations']['operations'][k]['rateType'])
        print(js_currency['props']['initialState']['operations']['operations'][k]['city']['name'])
        print(js_currency['props']['initialState']['operations']['operations'][k]['rate'])
        print('-----------------------------------------------------------------------------------')
    def ret(var):
        j_c=var
        len(j_c)
spec()