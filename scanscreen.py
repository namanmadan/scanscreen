import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

#Used headers/agent as the request timed out and asking for agent. Using following code you can fake the agent.
headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

url=[]
for i in range(1,9):
    response = requests.get("https://www.swiggy.com/chennai/omr-perungudi-restaurants?page="+str(i),headers=headers)
    content = response.content
    soup = BeautifulSoup(content,"html.parser")
    data = json.loads(soup.find('script', type='application/ld+json').text)
    dic=data['itemListElement']
    for i in range(len(dic)):
        a=dic[i]['url']
        url.append(a)


longitude=[]
latitude=[]
price=[]
for i in range(len(url)):
    response=requests.get(url[i])
    content=response.content
    soup=BeautifulSoup(content,"html.parser")
    data=json.loads(soup.find('script', type='application/ld+json').text)
    lon=data['geo']['longitude']
    lat=data['geo']['latitude']
    pri=data['priceRange']
    longitude.append(lon)
    latitude.append(lat)
    price.append(pri)


price_for_two=[]
for i in range(len(price)):
    en=price[i].encode('ascii','ignore')
    pr=int(filter(str.isdigit,en))
    price_for_two.append(pr)


swiggy=pd.DataFrame() 


swiggy['longitude']=longitude
swiggy['latitude']=latitude
swiggy['price']=price_for_two

swiggy.to_csv("scrape_new.csv",index=False)

