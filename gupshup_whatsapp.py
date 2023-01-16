#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:22:26 2022

@author: dragon
"""

# whatsapp messaging

import requests

headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    'apikey': 'w6hwq38eatdcxhh1rmspla35e7ljyqxg',
    'cache-control': 'no-cache',
}

message = 'Hello kiran broo, Guess Who I\'m ???'

msg = '%20'.join(i for i in message.split(' '))

# quick_reply
#data = 'channel=whatsapp&source=917834811114&destination=917036878295&message=%7B%22type%22:%22quick_reply%22,%22content%22:%7B%22type%22:%22text%22,%22text%22:%22Recharge%20Amount%22,%22caption%22:%22Select%20recharge%20amount%22%7D,%22options%22:%5B%7B%22type%22:%22text%22,%22title%22:%22$50%22%7D,%7B%22type%22:%22text%22,%22title%22:%22$100%22%7D,%7B%22type%22:%22text%22,%22title%22:%22$150%22%7D%5D%7D&src.name=krishnatest1'
# pdf sending
# data = 'channel=whatsapp&source=917834811114&destination=917036878295&message=%7B%22type%22:%22file%22,%22url%22:%22https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf%22,%22caption%22:%22this%20is%20pdf%20%22,%22filename%22:%22Sample.pdf%22%7D&src.name=krishnatest1'
# whatsapp text sending

data = f'channel=whatsapp&source=917834811114&destination=917019040630&message=%7B%22type%22:%22text%22,%22text%22:%22{msg}%22%7D&src.name=GupshupDemoAssert'

response = requests.post('https://api.gupshup.io/sm/api/v1/msg', headers=headers, data=data)

print(response.text)
