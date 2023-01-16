#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:32:11 2022

@author: dragon
"""

import os
import glob
removed = []
from_path = '/home/dragon/Documents/work/jnj/datasets/train/labels'

for txt in glob.glob(f'{from_path}/*.txt'):
    file = open(txt, "r")
    lines = file.readlines()
    lines = set(lines)
    with open(txt, 'w') as text:
        for line in lines:
            if not line.isspace():
                line = line.rstrip()
                text.write(line+'\n')
    file = open(txt, "r")
    lines = file.readlines()
    lines = set(lines)
    if len(lines)>0:
        for line in lines:
            if len(line.split(' '))<5 or len(line.split(' '))>5:
                removed.append(txt)
                os.remove(txt)
                break
    else:
        removed.append(txt)
        os.remove(txt)
print('Removed :-  ',len(removed))

