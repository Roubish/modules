#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 20:53:50 2022

@author: dragon
"""
import shutil

remove_path = '/home/dragon/removed_with_code'
import glob
texts_path = '/home/dragon/Downloads'
for txt in glob.glob(f'{texts_path}/*.txt'):
    lines = []
    with open(txt, 'r') as file:
        for line in file.readlines():
            word = line.split(' ')
            if word[0]=='9':
                shutil.move(txt,remove_path)
