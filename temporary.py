#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:15:21 2022

@author: dragon
"""

#%%
name = '/home/dragon/Downloads/lpd_20k_012345678/lpd_20k_task_0'
lst = name.split('/')[-1].split('.')
file = ' '.join(lst[:-1])
print(file)

#%%
from glob import glob
im_list = glob('/home/dragon/Downloads/lpd_20k_012345678/lpd_20k_task_0/*')
t = set()
for i in im_list:
  t.add(i.split('.')[-1])
print(t)
print(len(im_list))

#%%

from pdf2image import convert_from_path
pdf = '/home/dragon/Documents/rust/samvidhan.pdf'
pages = convert_from_path(pdf,0)
print("READED")
img_count = 1
filename = (pdf.replace('.pdf','')).split('/')
for page in pages:
    img_name = ("{}_img_"+str(img_count)+".jpg").format(filename[-1])
    page.save(img_name,'JPEG')
    img_count += 1
