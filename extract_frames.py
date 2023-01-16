#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:37:24 2022

@author: dragon
"""
import cv2
from glob import glob
video_list = glob('/home/dragon/Downloads/baddi_data/videos/*')

for video_path in video_list:
    cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(fps)
    lst = video_path.split('/')[-1].split('.')
    filename = ' '.join(lst[:-1])
    frame_num = 0
    while(cap.isOpened()):
        ret, frame = cap.read()                
        if not  ret:          
            print("end of the video file...")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            break
        if frame_num%fps==0:
            image_path = f'/home/dragon/Downloads/baddi_data/frames/{filename}_{frame_num}.jpg'
            cv2.imwrite(image_path, frame)
            print(f'saved frame {frame_num}')
        frame_num+=1


