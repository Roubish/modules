#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:33:26 2022

@author: dragon
"""

# JPEG PNG to JPG
import cv2
from glob import glob
import os
path = '/home/dragon/Documents/work/aarti_poc/arti_annotations'
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

#%%

# REMOVE CORRUPTED AND EMPTY ONES
import shutil
#import os
import glob
removed = []
from_path = '/home/dragon/Downloads/hul_task_1(done)'

remove_path = '/home/dragon/removed_with_code'
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
                shutil.move(txt,remove_path)
                #os.remove(txt)
                break
    else:
        removed.append(txt)
        shutil.move(txt,remove_path)
#        os.remove(txt)
print('Removed :-  ',len(removed))
#%%

# REMOVE NOT LISTED
# REMOVE NOT LISTED

import shutil
remove_path = '/home/dragon/removed_with_code'
import pathlib
import os
img_list = '/home/dragon/Downloads/HUL/frames/hul_task_1/'
text_list = '/home/dragon/Downloads/HUL/frames/hul_task_1/'

for image in os.listdir(img_list):
    file_extension = pathlib.Path(image).suffix
    if file_extension=='.txt':
        name = image.split('.')
        name[-1]='jpg'
        file = '.'.join(name)
        os.chdir(img_list)
        if file not in os.listdir(img_list):
            print('removed text :- ',image)
            shutil.move(image,remove_path)

#            os.remove(image)

    if file_extension=='.jpg':
        name = image.split('.')
        name[-1]='txt'
        file = '.'.join(name)
        os.chdir(img_list)
        if file not in os.listdir(text_list):
            print('removed image :- ',image)
            shutil.move(image,remove_path)

            #os.remove(image)

for image in os.listdir(text_list):
    file_extension = pathlib.Path(image).suffix
    if file_extension=='.txt':
        name = image.split('.')
        name[-1]='jpg'
        file = '.'.join(name)
        os.chdir(text_list)
        if file not in os.listdir(img_list):
            print('removed text :- ',image)
            shutil.move(image,remove_path)

            #os.remove(image)

    if file_extension=='.jpg':
        name = image.split('.')
        name[-1]='txt'
        file = '.'.join(name)
        os.chdir(text_list)
        if file not in os.listdir(text_list):
            print('removed image :- ',image)
            shutil.move(image,remove_path)

            #os.remove(image)

#%%

# MOVE FILES TO DATASETS
import shutil
from glob import glob
from_path = '/home/dragon/Documents/work/aarti_poc/datasets/train/mask_nomask'
imgs_path = '/home/dragon/Documents/work/aarti_poc/datasets/train/images'
lbls_path = '/home/dragon/Documents/work/aarti_poc/datasets/train/labels'

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
