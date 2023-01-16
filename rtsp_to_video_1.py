import cv2




video = 'rtsp://admin:Admin%40123@14.99.145.34:10554/streaming/channels/101/?transportmode=unicast'
cap = cv2.VideoCapture(video)
fps = int(cap.get(cv2.CAP_PROP_FPS))
writer = None
pixel_gray = []
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m_%d_%Y__%H_%M_%S")

while True:
    ret, frame = cap.read()
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        writer = cv2.VideoWriter(f'/home/dragon/Downloads/aarti_videos/{date_time}.avi', fourcc, fps, (width, height), True)
    if writer is not None:
        writer.write(frame)
        print("Writing frame...")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

    if not  ret:          
        print("end of the video file...")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        break
