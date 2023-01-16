#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:22:26 2022

@author: dragon
"""

# Email AUthorization

import requests

headers = {
    'Accept': 'application/json',
    'apikey': 'euvxovg7hpidwdiyejvoefkdjwzxti8b',
}

data = {
    'accountid': 'krishna.prasad@assertsecuretech.com',
    'token': 'PAISAKELIYE',
}

response = requests.put('https://api.gupshup.io/sm/api/ent/email/account', headers=headers, data=data)
print(response.text)


# Email sending

import requests

headers = {
    'Accept': 'application/json',
    'apikey': 'euvxovg7hpidwdiyejvoefkdjwzxti8b',
}

data = {
    'From': 'krishna.prasad@assertsecuretech.com',
    'Subject': 'TEST GUPSHUP',
    'Content': 'HELLO BROO',
    'Recipients': 'krishna.prasad@assertai.com',
    'scheduled_at': '',
}

response = requests.post('https://api.gupshup.io/sm/api/ent/email/msg', headers=headers, data=data)

print(response.text)
#%%

import requests

headers = {
    'Accept': 'text/html',
    'apikey': 'w6hwq38eatdcxhh1rmspla35e7ljyqxg',
}

data = {
    'channel': 'EMAIL',
    'source': 'kiran.naik@assertai.com',
    'destination': 'kirankumarsnaik@gamil.com',
    'message': '{"type":"text","text":"hello"}',
    'disablePreview': 'false',
}

response = requests.post('https://api.gupshup.io/sm/api/v1/msg', headers=headers, data=data)

print(response.text)
