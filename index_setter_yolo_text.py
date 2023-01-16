#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:54:11 2022

@author: dragon
"""

def replace_index(textfile,namesfile):
    with open(namesfile, "r") as f:
        dummy = [line.strip() for line in f.readlines()]
    with open(textfile, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    
    lines_set = set()
    for line in lines:
        ln_slt = line.split(' ')
        if dummy[int(ln_slt[0])]=='0':
            ln_slt[0]='0'
        elif dummy[int(ln_slt[0])]=='1':
            ln_slt[0]='1'
        elif dummy[int(ln_slt[0])]=='2':
            ln_slt[0]='2'
        elif dummy[int(ln_slt[0])]=='3':
            ln_slt[0]='3'
        elif dummy[int(ln_slt[0])]=='4':
            ln_slt[0]='4'
        elif dummy[int(ln_slt[0])]=='5':
            ln_slt[0]='5'
        elif dummy[int(ln_slt[0])]=='6':
            ln_slt[0]='6'
        elif dummy[int(ln_slt[0])]=='7':
            ln_slt[0]='7'
        elif dummy[int(ln_slt[0])]=='8':
            ln_slt[0]='8'
        elif dummy[int(ln_slt[0])]=='9':
            ln_slt[0]='9'
        elif dummy[int(ln_slt[0])]=='A':
            ln_slt[0]='10'
        elif dummy[int(ln_slt[0])]=='B':
            ln_slt[0]='11'
        elif dummy[int(ln_slt[0])]=='C':
            ln_slt[0]='12'
        elif dummy[int(ln_slt[0])]=='D':
            ln_slt[0]='13'
        elif dummy[int(ln_slt[0])]=='E':
            ln_slt[0]='14'
        elif dummy[int(ln_slt[0])]=='F':
            ln_slt[0]='15'
        elif dummy[int(ln_slt[0])]=='G':
            ln_slt[0]='16'
        elif dummy[int(ln_slt[0])]=='H':
            ln_slt[0]='17'
        elif dummy[int(ln_slt[0])]=='I':
            ln_slt[0]='18'
        elif dummy[int(ln_slt[0])]=='J':
            ln_slt[0]='19'
        elif dummy[int(ln_slt[0])]=='K':
            ln_slt[0]='20'
        elif dummy[int(ln_slt[0])]=='L':
            ln_slt[0]='21'
        elif dummy[int(ln_slt[0])]=='M':
            ln_slt[0]='22'
        elif dummy[int(ln_slt[0])]=='N':
            ln_slt[0]='23'
        elif dummy[int(ln_slt[0])]=='O':
            ln_slt[0]='24'
        elif dummy[int(ln_slt[0])]=='P':
            ln_slt[0]='25'
        elif dummy[int(ln_slt[0])]=='Q':
            ln_slt[0]='26'
        elif dummy[int(ln_slt[0])]=='R':
            ln_slt[0]='27'
        elif dummy[int(ln_slt[0])]=='S':
            ln_slt[0]='28'
        elif dummy[int(ln_slt[0])]=='T':
            ln_slt[0]='29'
        elif dummy[int(ln_slt[0])]=='U':
            ln_slt[0]='30'
        elif dummy[int(ln_slt[0])]=='V':
            ln_slt[0]='31'
        elif dummy[int(ln_slt[0])]=='W':
            ln_slt[0]='32'
        elif dummy[int(ln_slt[0])]=='X':
            ln_slt[0]='33'
        elif dummy[int(ln_slt[0])]=='Y':
            ln_slt[0]='34'
        elif dummy[int(ln_slt[0])]=='Z':
            ln_slt[0]='35'
        word = ' '.join(ln_slt)
        lines_set.add(word)
    
    file1 = open(textfile, "w")
    for line in lines_set:
        file1.write(f"{line} \n")
    file1.close()

from glob import glob
namesfile = "/home/dragon/Downloads/task1/obj.names"
for textfile in glob('/home/dragon/Downloads/task1/obj_train_data/*.txt'):
    print('writing ',textfile)
    replace_index(textfile,namesfile)
    print('Done ',textfile)

#%%
def replace_index_everywhere(textfile,namesfile):
    with open(namesfile, "r") as f:
        dummy = [line.strip() for line in f.readlines()]
    with open(textfile, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    
    lines_set = set()
    for line in lines:
        ln_slt = line.split(' ')
        if dummy[int(ln_slt[0])]=='Animal':
            ln_slt[0]='0'
        elif dummy[int(ln_slt[0])]=='People':
            ln_slt[0]='1'
        elif dummy[int(ln_slt[0])]=='Biker_without_helmet':
            ln_slt[0]='2'
        elif dummy[int(ln_slt[0])]=='Biker_with_helmet':
            ln_slt[0]='3'
        elif dummy[int(ln_slt[0])]=='Dock_open':
            ln_slt[0]='4'
        elif dummy[int(ln_slt[0])]=='Dock_close':
            ln_slt[0]='5'
        elif dummy[int(ln_slt[0])]=='Emergency_gate_open':
            ln_slt[0]='6'
        elif dummy[int(ln_slt[0])]=='Emergency_gate_close':
            ln_slt[0]='7'
        elif dummy[int(ln_slt[0])]=='Vehicle':
            ln_slt[0]='8'
        word = ' '.join(ln_slt)
        lines_set.add(word)
    
    file1 = open(textfile, "w")
    for line in lines_set:
        file1.write(f"{line} \n")
    file1.close()

from glob import glob
namesfile = "/home/dragon/Downloads/Drone_annotated_data/wrong/egi/obj.names"
for textfile in glob('/home/dragon/Downloads/Drone_annotated_data/wrong/egi/obj_train_data/*.txt'):
    print('writing ',textfile)
    replace_index_everywhere(textfile,namesfile)
    print('Done ',textfile)


