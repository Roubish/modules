#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:09:23 2022

@author: dragon
"""

file_path = '/home/dragon/Documents/work/guard/yolov5-5.0/requirements_yolov5 (copy).txt'
lines = []
with open(file_path, 'r') as file:
    for line in file.readlines():
        word = line.split('@')
        word=word[0]
        #word[0]='"'+word[0]+'"'
        #word[1]='"'+word[1]+'"'
        lines.append(''.join(word))

with open(file_path, 'w') as file:
    for line in lines:
        file.write(line+'\n')

#%%
import cv2
file_path = '/home/dragon/Documents/work/mahindra_logistics/yolov5-6.1/runs/detect/exp5/text_file_51_images (copy).txt'

import os
#lst_files = os.listdir('/home/dragon/Documents/work/mahindra_logistics/yolov5-6.1/runs/detect/exp5/crops/non_faulty')
with open(file_path, 'r') as textfile:
    for file in lst_files:
        textfile.write(file+"\t"+"\"TVFD1N1\""+'\n')
        print(file)
    path = f'/home/dragon/Downloads/boxes/{file}'
    image = cv2.imread(path)
    file = file.split('.')
    file[0] = 'kshitij_ocr_'+file[0]
    file = '.'.join(file)
    cv2.imwrite(file, image)
    os.remove(path)
    print('removed:- ',file)

#%%

file_path = '/home/dragon/Documents/work/mahindra_logistics/yolov5-6.1/runs/detect/exp5/text_file_51_images (copy).txt'
lines = []
linez = []
with open(file_path, 'r') as file:
    linez = file.readlines()
print(len(linez))
linez = set(linez)
print(len(linez))

with open(file_path, 'w') as file:
    for line in linez:
        file.write(line+'\n')


#%%

import glob
list_files = glob.glob('/home/dragon/Downloads/HUL/frames/hul_task_0/*.txt')
classes = ['Door_open','Door_Close','Uniform','without_uniform','Gloves','Bare_Hand','Head_Net']
for file_path in list_files:
    lines = []
    with open(file_path, 'r') as file:
        linez = file.readlines()
        for i in range(len(linez)):
            lst = linez[i].split(' ')
            if classes[int(lst[0])]=='Door_Close':
                lst[0] = '0'

            lines.append(' '.join(lst))
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)

