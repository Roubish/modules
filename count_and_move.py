#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:39:43 2022

@author: dragon
"""


## Number of Items in a folder
## Number of Items in a folder

from glob import glob
target_path = '/home/dragon/Downloads/lpd_data'
destination_path = '/home/dragon/Downloads/lpd_data'

folders_list = glob(f'{target_path}/*')
for folder in folders_list:
    folder_list = glob(folder+'/*')
    lst = folder.split('/')
    folder = ''.join(lst[-1])
    print(folder +" is "+ str(len(folder_list)))


#%%
import shutil

from glob import glob
#folders_list = glob(f'{target_path}/*')
for folder in folders_list:
    folder_list = glob(folder+'/*')
    for image in folder_list:
        shutil.move(image,f'{destination_path}')

