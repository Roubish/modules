#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 05:21:31 2020

@author: vb
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd

def Get_data(no):
    page = urlopen('https://www.flipkart.com/search?q=latest+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=latest+mobiles%7CMobiles&requestId=91c6e91e-f7ef-4b4b-a61b-486366b7605b&as-backfill=on&page=' + str(no))
    soup = bs(page,'lxml')
    mobiles=[] 
    for r in soup.findAll('div', attrs = {'class':"_1UoZlX"}):
        expt_img = r.find('div', attrs={'class':'_1-2Iqu row'})
        name = r.find('div', attrs={'class':'_3wU53n'})
#        images = r.find('div', attrs={'class':'_3BTv9X'})
        rating = r.find('span', attrs={'class':'_2_KrJI'})
        user_rated = r.find('span', attrs={'class':'_38sUEc'})
        
        
        alls=[]
        if expt_img is not None:
            alls.append(expt_img.text)
        else:
            alls.append('try again rarey')
            
        if name is not None:
            alls.append(name.text)
        else:
            alls.append('unknown_product')
        
        if user_rated is not None:
            alls.append(user_rated.text)
        else:
            alls.append('user_rated not found')

        if rating is not None:
            alls.append(rating.text)
        else:
            alls.append('-1')

    for img in soup.findAll('div', attrs = {'class':"_1UoZlX"}):
            images = img.find('div', attrs={'class':'_3BTv9X'})
            alls.append(images.get('src'))
            mobiles.append(alls)
    return mobiles
results = []
for i in range(0,1):
    results.append(Get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results), columns=['expt_img','name','user_rated','rating','images'])
df.to_csv('flipkart_lat_mob.csv', index=False,encoding='UTF-8')
