#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:51:59 2023

@author: dragon
"""

import cv2
video_capture = cv2.VideoCapture(0)
frame_num = 0
while True:
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #lst = imagePath.split('/')[-1].split('.')
    #file = '.'.join(lst[:-1])
    #frame_num+=1
    #cv2.imwrite(f"{frame_num}_detected.jpg", frames)
    
video_capture.release()
cv2.destroyAllWindows()
