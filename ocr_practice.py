#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:54:05 2022

@author: dragon
"""

import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('/home/dragon/Downloads/DSC07872.JPG', detail = 0)

print(result)
#%%
from PIL import Image
import pytesseract
import numpy as np
filename = '/home/dragon/Downloads/20210428_18_18_35_000_uA7x1XuBPngcHFRu7KambGvmgt62_F_5632_4224 (copy).jpeg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print (text)
#%%
import easyocr

reader = easyocr.Reader(['en', 'ko'])
result = reader.readtext('/home/dragon/Downloads/20210428_18_18_35_000_uA7x1XuBPngcHFRu7KambGvmgt62_F_5632_4224 (copy).jpeg')
print(result)
#%%
from PIL import Image
import pytesseract
import numpy as np
filename = '/home/dragon/Downloads/20210428_18_18_35_000_uA7x1XuBPngcHFRu7KambGvmgt62_F_5632_4224 (copy).jpeg'
img2 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img2)
print(text)
#%%
# import the necessary packages
import pytesseract
import argparse
import cv2
# construct the argument parser and parse the arguments}
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="/home/dragon/Pictures/Screenshot from 2022-07-27 12-53-55.png")
args = vars(ap.parse_args())
# load the input image and convert it from BGR to RGB channel
# ordering}
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
text = pytesseract.image_to_string(image)
print(text)
