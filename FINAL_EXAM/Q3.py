#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv

cap = cv.VideoCapture('Q_three.AVI')
ret, first_frame = cap.read()
avg = np.zeros(first_frame.shape, np.float32)
k = 0

while(cap.isOpened()):

    ret, frame = cap.read()
    
    if ret == True:
        avg += frame
        k = k+1   
   
    else:
        
        break

cap.release()
cv.destroyAllWindows()

avg = avg / k
avg = cv.cvtColor(avg, cv.COLOR_BGR2GRAY)
avg = np.array(avg, dtype = 'uint8')


cap = cv.VideoCapture('Q_three.AVI')
ret, first_frame = cap.read()

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
        difference = cv.absdiff(avg, gray_frame)
        difference = cv.threshold(difference, 50, 255, cv.THRESH_BINARY)[1]
        #cv.imshow('Difference', difference)
        #cv.waitKey(30)  
        cv.imshow('diff', difference)
        cv.waitKey(30) 
    
        frame[np.where(difference == 255)] = (0, 0, 255)
        cv.imshow('frame', frame)
        cv.waitKey(30) 
    else:
        break

        
cap.release()
cv.destroyAllWindows()








# In[ ]:





# In[ ]:




