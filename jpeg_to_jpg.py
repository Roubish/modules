#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:59:03 2022

@author: dragon
"""


import cv2
from glob import glob
import os
path = '/home/dragon/Downloads/lpd_data'
target = f'{path}/*.jpeg'
for img in glob(target):
    image = cv2.imread(img)
    lst = img.split('.')
    file = '.'.join(lst[:-1])
    cv2.imwrite(f'{file}.jpg', image)
    print(img)
    os.remove(img)
target = f'{path}/*.png'
for img in glob(target):
    image = cv2.imread(img)
    lst = img.split('.')
    file = '.'.join(lst[:-1])
    cv2.imwrite(f'{file}.jpg', image)
    print(img)
    os.remove(img)




