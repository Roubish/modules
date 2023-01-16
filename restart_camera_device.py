#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:44:11 2022

@author: dragon
"""

import os
import time
import psutil
import datetime
start = datetime.time(0, 0, 0)
end = datetime.time(23, 45, 0)
while True:
    try:
        ds = []
        for proc in psutil.process_iter():
            procc = proc.cmdline()
            # sudo python3 deepstream-intrusion.py uri uri folder_name
            if len(procc) >= 2 and "python3" in procc and "deepstream-vehicle.py" in procc:
                ds.append(proc.pid)
        # CHECK THE TIME CONDITION HERE
        current = datetime.datetime.now().time()
        if start <= current and current <= end:  # RUN TIME
            print("inside time")
            if len(ds) == 0:  # RUN IF IT IS NOT RUNNING
                print("Opening Frames")
                os.system("sh run_vehicle.sh")
                # os.system("/home/assert-arya/scripts/run_intrusion.sh &")
        else:  # CLOSE TIME
            if len(ds) > 0:
                print("Closing DeepStream")
                for pid in ds:
                    os.system("sudo kill -15 " + str(pid))
        time.sleep(5)  # CHECK IN EACH 5 SECONDS
    except KeyboardInterrupt:
        break
cd /home/$USER/jetson-AI/python/Arya_Shutter_Prod/
python3 shutter1.py --model=../training/detection/ssd/models/shutter_arya/ssd-mobilenet.onnx --labels=../training/detection/ssd/models/shutter_arya/labels.txt -input-blob=input_0 --output-cvg=scores --output-bbox=boxes --threshold=0.85 --input-codec=h265 rtsp://admin:assert%40123@192.168.1.2:554/h265/main/ch4/main/av_stream --headless
