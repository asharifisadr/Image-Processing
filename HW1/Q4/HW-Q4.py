#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2 as cv
import numpy as np 

 #Capture Video from webcam 

webcam_video = cv.VideoCapture(0)

# making space for putting previous frame to comparison with mew frame    

ex_frame = None  

#  while for show as a video
while True:
# check if loaded currectly        
    check, frame = webcam_video.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_frame = cv.GaussianBlur(gray_frame,(11,11),0)
# put gray fram in ex frame for the first time         
    if ex_frame is None :
        ex_frame = gray_frame
# make array from diffrence of new fram and ex fram ( two consecutive frames)        
    diff_frame = cv.absdiff(ex_frame, gray_frame)
    ex_frame=gray_frame

#Thresolding diff frame

    threshold_frame = cv.threshold(diff_frame, 10, 255, cv.THRESH_BINARY)
# Alarm if detect motion 
    if np.average(diff_frame)>=10:
        print('Motion')
# show thresholding video
    cv.imshow('Capturing', threshold_frame[1])
 

 # Set q = quit

    key = cv.waitKey(1)
    if(key == ord('q')):
        break
 

webcam_video.release()

cv.destroyAllWindows


# In[ ]:





# In[ ]:




