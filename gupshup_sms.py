#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:22:26 2022

@author: dragon
"""

# normal messaging

import requests

headers = {
    'Authorization': 'euvxovg7hpidwdiyejvoefkdjwzxti8b',
    'Content-Type': 'application/x-www-form-urlencoded',
}

message = 'Hello broo, How are you ???'

data = f'destination=+917036878295&message={message}&source=GSDSMS'

response = requests.post('https://api.gupshup.io/sms/v1/message/168dcfd9-4461-4864-866f-cb2c81690421', headers=headers, data=data)

print(response.text)

#%%

import requests

headers = {
    'apikey': 'euvxovg7hpidwdiyejvoefkdjwzxti8b',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'route=soip&source=smsbot172900&destination=917036878295&message=hello bro this is sms from gupshup RCS'

response = requests.post('https://botplatform.gupshup.io/bot/message/v3/818c3740-d17f-11e5-ae2d-0ea1b0410657/msg', headers=headers, data=data)
print(response.text)
