import requests
from bs4 import BeautifulSoup
import lxml

url = input('input url:')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",

    "Accept-Language": "en" }

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")

def checkPrice ():    
    title = soup.select_one("span[id='productTitle']").text
    title = title.strip()
    print(title)
    price = soup.select_one("span[class='a-offscreen']").text
    print(price)
    priceNumber = float(price.replace('$',''))
    minprice =float(input('input minimum price you can afford: '))
    if (priceNumber < minprice) :
            print('BUY BUY BUY')
    else :
            print('cannot afford')
        
checkPrice()