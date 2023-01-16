#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:20:31 2022

@author: dragon
"""


from itertools import islice
from glob import glob
import shutil
import os

main_path = '/home/dragon/Downloads/HUL/frames'
prefix = 'hul_task_'
length_to_split = [2923,2600]

Input = glob(f'{main_path}/*')

Inputt = iter(Input)
Output = [list(islice(Inputt, elem))
        for elem in length_to_split]

for i in range(len(Output)):
    leng = str(len(Output[i]))
    if leng not in os.listdir(main_path):
      os.mkdir(f'{main_path}/{prefix}{i}')

    for from_path in Output[i]:
        shutil.move(from_path,f'{main_path}/{prefix}{i}')
