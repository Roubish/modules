#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:21:35 2022

@author: dragon
"""

import shutil
import glob
texts_path = '/home/dragon/Documents/work/mahindra_logistics/datasets/train/labels'
move_path = '/home/dragon/Documents/work/mahindra_logistics/tao_voc/data/split/train'
classes = ['intact_carton_box','damage_carton_box','intact_sack','damage_sack']
for txt in glob.glob(f'{texts_path}/*.txt'):
    lst = txt.split('/')
    filename = ''.join(lst[-1])
    print(filename)
    lines = []
    with open(txt, 'r') as file:
        for line in file.readlines():
            word = line.split(' ')
            for i in range(len(classes)):
                if int(word[0])==i:
                    shutil.copyfile(txt,f'{move_path}/{classes[i]}/{filename}')
                    print(f'Copied succesfully to {classes[i]}')


#%%                    

import shutil
import os

some_texts = '/home/dragon/Documents/work/mahindra_logistics/datasets/train/labels'
full_images = '/home/dragon/Documents/work/mahindra_logistics/datasets/train/images'
classes = ['intact_carton_box','damage_carton_box','intact_sack','damage_sack']

for path in os.listdir(some_texts):
    lst = path.split('.')
    file = '.'.join(lst[:-1])
    print(file)

    shutil.copyfile(f"{full_images}/{file}.jpg",f'{some_texts}/{file}.jpg')
    print(f'Copied succesfully to {some_texts}')

