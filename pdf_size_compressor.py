#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:08:22 2022

@author: dragon
"""
import glob
from pdf2image import convert_from_path
import os
import img2pdf
from PIL import Image

cwd = os.getcwd()
pdf = '/home/dragon/Downloads/AdmitCard-223510285779.pdf'
pages = convert_from_path(pdf,0)
img_count = 1
lst = pdf.split('/')[-1].split('.')
pdfname = '.'.join(lst[:-1])

for page in pages:
    img_name = ("{}_img_"+str(img_count)+".jpg").format(pdfname)
    page.save(img_name,'JPEG')
    img_count += 1
    print(img_name,"image saved")
    img = Image.open(img_name)
    filename = f"Compressed_{img_name}"
    img.save(filename, 
                 "JPEG", 
                 optimize = True, 
                 quality = 50)
    os.remove(img_name)
pdf_name = ("/home/dragon/Downloads/devi1_{}.pdf").format(pdfname)
with open(pdf_name,'wb') as creat_pdf:
    pdf_bytes = img2pdf.convert(sorted(glob.glob("*.jpg")))
    creat_pdf.write(pdf_bytes)
creat_pdf.close()

for file in glob.glob("*.jpg"):
    os.remove(str(file))

