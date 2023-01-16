#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 05:21:31 2020

@author: vb
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def Get_data(no):
    page = requests.get('https://www.flipkart.com/search?q=latest+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=latest+mobiles%7CMobiles&requestId=91c6e91e-f7ef-4b4b-a61b-486366b7605b&as-backfill=on&page=' + str(no))
    soup = bs(page.content,'lxml')
    mobiles=[] 
    for r in soup.findAll('div', attrs = {'class':"_1UoZlX"}):
        name = r.find('div', attrs={'class':'_3wU53n'})
        rating = r.find('span', attrs={'class':'_2_KrJI'})
        img = r.find('div', attrs={'class':'_3BTv9X'})
        user_rated = r.find('span', attrs={'class':'_38sUEc'})
        
        alls=[]
            
        if name is not None:
            alls.append(name.text)
        else:
            alls.append('unknown_product')
        
        if img is not None:
            alls.append(img.get)
        else:
            alls.append('img not found')

        if user_rated is not None:
            alls.append(user_rated.text)
        else:
            alls.append('user_rated not found')

        if rating is not None:
            alls.append(rating.text)
        else:
            alls.append('-1')
        mobiles.append(alls)
    
    return mobiles
results = []
for i in range(0,100):
    results.append(Get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results), columns=['name','img','user_rated','rating'])
df.to_csv('flipkart_lat_mob.csv', index=False,encoding='UTF-8')
