import random
import numpy as np
import cv2
 
cap = cv2.VideoCapture('cars.mp4')

totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frames = []
count_frame=0
while True:
    randomFrameNumber=random.randint(0, totalFrames)
    cap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, frame = cap.read()
    if success:
        count_frame+=1
        frames.append(frame)
    if count_frame==30:
        break
 
Frame = np.median(frames, axis=0).astype(dtype=np.uint8)  

cv2.imshow('Background_Estimation', Frame)
cv2.imwrite("Road_Without_Car.jpg",Frame)
cv2.waitKey(0)