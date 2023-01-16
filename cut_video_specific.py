#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:37:01 2022

@author: dragon
"""
import cv2

video_path = "/home/dragon/Downloads/Azad Hind Fauj Diwas  21st Oct 1943  Netaji Subhas Chandra Bose  INA  BEFOJJI  SURAT.mp4"

cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))
font = cv2.FONT_HERSHEY_SIMPLEX
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('/home/dragon/Downloads/Azad_Hind_Flag.avi', fourcc, fps, (width, height))


frame_num = 0
start = 270
end = 900
while(cap.isOpened()):
    ret, frame = cap.read()                
# =============================================================================
#     if not  ret:          
#         print("end of the video file...")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#         break
# =============================================================================
    if frame_num>=start and frame_num<=end:
        output_movie.write(frame)
        print(f'wrote frame {frame_num}')
    frame_num+=1
    if frame_num>end:
#    if not  ret:          
        print("video cutting completed...")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        break
