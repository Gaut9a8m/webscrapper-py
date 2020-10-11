import requests
from bs4 import BeautifulSoup
import math

url_a= 'https://www.amazon.in/Hindware-Auto-Clean-Nevio-60/dp/B01I94AYKY/ref=sr_1_2?crid=2Z42O2VFOAAEK&dchild=1&keywords=hindware+nevio+plus+60+auto-clean&qid=1602407547&sprefix=Hindware+Nevio+Plus+60+%2Caps%2C352&sr=8-2'
url_f = 'https://www.flipkart.com/hindware-nevio-plus-60-auto-clean-wall-mounted-chimney/p/itm61b56daf8240e?pid=CHYFJK3YVWEVHVZD&lid=LSTCHYFJK3YVWEVHVZDLQOGUB&marketplace=FLIPKART'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'} 


def check_price():
    try:
        page_a = requests.get(url_a,headers=headers)
        page_f = requests.get(url_f,headers=headers)
        
        soup_a = BeautifulSoup(page_a.text,'html.parser')
        soup_f = BeautifulSoup(page_f.text,'html.parser')

        # followers = soup.find(class_="-nal3")
        meta_f = soup_f.find(class_="_1vC4OE _3qQ9m1").get_text()[1:]
        price_f = int("".join(meta_f.split(",")))
        
        
        meta_a = soup_a.find(id="priceblock_ourprice").get_text()[2:8]
        # print(meta_a)
        price_a = int("".join(meta_a.split(",")))
        
        if(price_a>price_f):
            print("Buy from flipkart:Rs. {}".format(price_f))
        else:
            print("Buy from Aamazon:rs. {}".format(price_a))
        print("Flipkart price: {}, Amazon price: {}".format(price_f,price_a))
    except:
        print('something went wrong:')

if __name__ == "__main__":
    check_price()