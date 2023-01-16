#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:19:12 2022

@author: dragon
"""

import json
import os
os.chdir('/home/dragon/Downloads/')
f = open('aarti.json')
os.chdir('/home/dragon/Documents/work/aarti_poc/datasets/new')

data = json.load(f)
for i in range(len(data)):
    print(data[i]['image'])
    comm = f"wget {data[i]['image']}"
    os.system(comm)
 
#f.close()
