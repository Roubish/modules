#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:02:47 2022

@author: dragon
"""


import pathlib
import os
img_list = '/home/dragon/Documents/work/hul/datasets/train/images/'
text_list = '/home/dragon/Documents/work/hul/datasets/train/labels/'

for image in os.listdir(img_list):
    file_extension = pathlib.Path(image).suffix
    if file_extension=='.txt':
        name = image.split('.')
        name[-1]='jpg'
        file = '.'.join(name)
        os.chdir(img_list)
        if file not in os.listdir(img_list):
            print('text is  ',image)
            os.remove(image)

    if file_extension=='.jpg':
        name = image.split('.')
        name[-1]='txt'
        file = '.'.join(name)
        os.chdir(img_list)
        if file not in os.listdir(text_list):
            print('image is  ',image)
            os.remove(image)

for image in os.listdir(text_list):
    file_extension = pathlib.Path(image).suffix
    if file_extension=='.txt':
        name = image.split('.')
        name[-1]='jpg'
        file = '.'.join(name)
        os.chdir(text_list)
        if file not in os.listdir(img_list):
            print('text is  ',image)
            os.remove(image)

    if file_extension=='.jpg':
        name = image.split('.')
        name[-1]='txt'
        file = '.'.join(name)
        os.chdir(text_list)
        if file not in os.listdir(text_list):
            print('image is  ',image)
            os.remove(image)

