#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:11:40 2022

@author: dragon
"""


import shutil
import glob
texts_path = '/home/dragon/Documents/work/mahindra_logistics/datasets/train/labels'
move_path = '/home/dragon/Documents/work/mahindra_logistics/tao_voc/data/split/train'

classes = ['intact_carton_box','damage_carton_box','intact_sack','damage_sack']
for txt in glob.glob(f'{texts_path}/*.txt'):
#    txt = '/home/dragon/Documents/work/mahindra_logistics/datasets/train/labels/7140.txt'
    text_name = txt.split('/')[-1].split('.')[:-1]
    img_name = '.'.join(text_name)
    filename = f"/home/dragon/Documents/work/mahindra_logistics/datasets/train/images/{img_name}.jpg"
    print(filename)
    lines = []
    with open(txt, 'r') as file:
        for line in file.readlines():
            word = line.split(' ')
            for i in range(len(classes)):
                if int(word[0])==i:
                    shutil.copyfile(filename,f'{move_path}/{classes[i]}/{img_name}.jpg')
                    print(f'Copied succesfully to {classes[i]}')

#%%

