#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:37:58 2022

@author: dragon
"""


import shutil
import glob
import os
extra_path = '/home/dragon/Downloads/HUL/frames/hul_task_0'
check_path = '/home/dragon/Downloads/HUL/frames/sailaja'
empty_path = '/home/dragon/Downloads/HUL/frames/krishna'
empty_list = []
for file in os.listdir(extra_path):
    if file in os.listdir(check_path):
        empty_list.append(file)
        path = f"{extra_path}/{file}"
        shutil.move(path,empty_path)
        print(path)
