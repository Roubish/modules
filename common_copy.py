#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:11:24 2022

@author: dragon
"""


import shutil
import os

val_images = '/home/dragon/Documents/work/hul/datasets/val/images/'
val_labels = '/home/dragon/Documents/work/hul/datasets/val/labels'
train_labels = '/home/dragon/Documents/work/hul/datasets/train/labels'

for path in os.listdir(val_images):
    lst = path.split('.')
    file = '.'.join(lst[:-1])
    
    shutil.copyfile(f"{train_labels}/{file}.txt",f'{val_labels}/{file}.txt')
    print('copied',f"{train_labels}/{file}.txt")

