#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:32:12 2022

@author: dragon
"""


from PyPDF2 import PdfFileMerger
merger = PdfFileMerger()
pdf_files = ["/home/dragon/Downloads/100-workouts/vol1.pdf",
"/home/dragon/Downloads/100-workouts/vol2.pdf",
"/home/dragon/Downloads/100-workouts/vol3.pdf",
"/home/dragon/Downloads/100-workouts/vol4.pdf"]
for pdf_file in pdf_files:
    merger.append(pdf_file)
merger.write("400-workouts.pdf")
merger.close()
