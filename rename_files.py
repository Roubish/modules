#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:43:32 2022

@author: dragon
"""

import os
import cv2
import pathlib

files_path = '/home/dragon/Downloads/A08_IFC2(PALLET_WITH_PERSON)/'
preffix = 'dup_1_2_'
os.chdir(files_path)
list_files = os.listdir(files_path)
for file in list_files:
    file_extension = pathlib.Path(file).suffix
    if file_extension in ('.jpeg','.jpg','.png'):
        name = preffix+file
        imread = cv2.imread(file)
        cv2.imwrite(name, imread)
        print('renamed as', name)
        #os.remove(file)
    if file_extension=='.txt':
        with open(file, 'r') as text:
            lines = text.readlines()
        name = preffix+file
        with open(name, 'w') as text:
            for line in lines:
                text.write(line+'\n')
        print('renamed as', name)
        #os.remove(file)

