#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:01:40 2022

@author: dragon
"""

import shutil
from glob import glob
from_path = '/home/dragon/Downloads/mumbai-port'
imgs_path = '/home/dragon/Documents/work/mumbai-port/datasets/train/images'
lbls_path = '/home/dragon/Documents/work/mumbai-port/datasets/train/labels'

for path in glob(f'{from_path}/*.jpg'):
    shutil.move(path,imgs_path)
    print('moved')
print(len(glob(f'{from_path}/*.jpeg')))
for path in glob(f'{from_path}/*.jpeg'):
    shutil.move(path,imgs_path)
    print('moved')
print(len(glob(f'{from_path}/*.png')))
for path in glob(f'{from_path}/*.png'):
    shutil.move(path,imgs_path)
    print('moved')
print(len(glob(f'{from_path}/*.txt')))
for path in glob(f'{from_path}/*.txt'):
    shutil.move(path,lbls_path)
    print('moved')
