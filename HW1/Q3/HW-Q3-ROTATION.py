#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv
import math
import numpy as np

# reading original image
img = cv.imread('C:/Users/Asus/Desktop/image/T.jpg',)
# specify my parameters  
angle = 60.0
x = img.shape[0]/2
y = img.shape[1]/2  
# making new array for putting result images after rotate operation 
ForwardMap  = np.zeros(img.shape, img.dtype)
BackwardMap = np.zeros(img.shape, img.dtype)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
# forward mapping
        forward_x = (i - x) * math.cos(angle*(math.pi/180)) - (j - y) * math.sin(angle*(math.pi/180)) + x
        forward_y = (i - x) * math.sin(angle*(math.pi/180)) + (j - y) * math.cos(angle*(math.pi/180)) + x
        forward_x = int(forward_x)
        forward_y = int(forward_y)
        
# backward mapping 
        backward_x = (i - x) * math.cos(angle*(math.pi/180)) + (j - y) * math.sin(angle*(math.pi/180)) + x
        backward_y = -(i - x) * math.sin(angle*(math.pi/180)) + (j - y) * math.cos(angle*(math.pi/180)) + x
        backward_x = int(backward_x)
        backward_y = int(backward_y)
# checking that new datas be in our range             
        if forward_x in range(img.shape[0]) and forward_y in range(img.shape[1]):
            ForwardMap[i, j] = img[forward_x, forward_y]
        else:
            pass
        if backward_x in range(img.shape[0]) and backward_y in range(img.shape[1]):
            BackwardMap[i, j] = img[backward_x, backward_y]
        else:
            pass
cv.imshow('orignal image',img)
cv.imwrite('C:/Users/Asus/Desktop/image/Forward Mapping.jpg', ForwardMap)
cv.imwrite('C:/Users/Asus/Desktop/image/Backward Mapping.jpg', BackwardMap)
cv.waitKey(0)
cv.destroyAllWindows()

