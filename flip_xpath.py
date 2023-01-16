import requests
from lxml import html
import pandas as pd
import datetime
from fake_headers import Headers


cources = []
colleges = []

header = Headers(headers=False).generate()
#print(header)
for no in range(1,3):
    web = requests.get('https://parenting.firstcry.com/articles/100-unique-baby-boy-names-inspired-by-lord-krishna/',headers=header)
    page = html.fromstring(web.content)
    for i in range(2,1000):
        cource = page.xpath('//*[@id="post-129505"]/div[2]/table/tbody/tr[{}]/td[1]/a/text()'.format(i))
        college = page.xpath('//*[@id="post-129505"]/div[2]/table/tbody/tr[{}]/td[2]/text()'.format(i))
        cources.append(''.join([str(pri) for pri in cource]))
        colleges.append(''.join([str(pri) for pri in college]))
cources = list(filter(None,cources))
cources = list(set(cources))
print(sorted(cources))
print()
print()
colleges = list(filter(None,colleges))
colleges = list(set(colleges))
print(sorted(colleges))

#%%


import requests
from lxml import html
from fake_headers import Headers

names = []
header = Headers(headers=False).generate()
web = requests.get('https://www.google.com/search?q=bike%20number%20plate%20images&tbm=isch&tbs=rimg:CTMUulvYJzHKYWx0sKhoImfu8AEAsgIOCgIIABAAKAE6BAgBEAE&hl=en&sa=X&ved=0CB0QuIIBahcKEwjQ9u6F45H7AhUAAAAAHQAAAAAQBw&biw=1905&bih=948',headers=header)
page = html.fromstring(web.content)
for i in range(0,10000):
    name = page.xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{}]/a[1]/div[1]/img'.format(i))
    names.append(name)
print(names)

#%%

import requests
from bs4 import BeautifulSoup
import csv
   
URL = "http://www.values.com/inspirational-quotes"
r = requests.get('https://www.google.com/search?q=bike%20number%20plate%20images&tbm=isch&tbs=rimg:CTMUulvYJzHKYWx0sKhoImfu8AEAsgIOCgIIABAAKAE6BAgBEAE&hl=en&sa=X&ved=0CB0QuIIBahcKEwjQ9u6F45H7AhUAAAAAHQAAAAAQBw&biw=1905&bih=948',headers=header)
   
soup = BeautifulSoup(r.content, 'html5lib')

quotes=[]  # a list to store quotes

table = soup.find('a', attrs = {'class' : 'wXeWr islib nfEiy'}) 

for row in table.findAll('img',
                         attrs = {'class':'rg_i Q4LuWd'}):
    quote = {}
    quote['image'] = row.h5.img
    quotes.append(quote)
   
        
