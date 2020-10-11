import requests
from bs4 import BeautifulSoup
import math
import signal
import time 


url = 'https://www.instagram.com/YOUR USER NAME'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'} 



def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)
interrupted = False

def check_follower():
    try:
        page = requests.get(url,headers=headers)
        
        soup = BeautifulSoup(page.text,'html.parser')

        # followers = soup.find(class_="-nal3")
        meta = soup.find("meta",property='og:description')
        raw_data = meta.attrs['content']
        raw_data =raw_data.split('-')
        raw_data = raw_data[0].split(' ')[0]
        # num = raw_data[0]
        num="".join(raw_data.split(","))
        l = len(num)
        followers=int(num)
        milestone = math.ceil(followers/(10**(l-1)))*(10**(l-1))
        if followers == milestone:
            print("Congrats!!!!!!!!!!!! you reached: {}".format(followers))
        else:
            print("Followers: {}, Next Milestone: {}".format(followers,milestone))
        # print(followers,milestone)
        # print(f)
    except:
        print('something went wrong:')

if __name__ == "__main__":
    
    while True:
        print("checking...")
        time.sleep(1)
        check_follower()   
        time.sleep(60)
            

        if interrupted:
            print("Exit...")
            break