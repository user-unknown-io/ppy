from requests import get
from bs4 import BeautifulSoup as Bs

def get_stock_price(stock:str)->float:
     url:str = f'https://www.google.com/finance/quote/{stock}:NSE'
     res = get(url)
     sou = Bs(res.text, 'html.parser')
     class1 = "YMlKec fxKbKc"
     price = float(sou.find(class_=class1).text.strip()[1:].replace(",",""))

     return price

a = get_stock_price('bse')

print(a)
