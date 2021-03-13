#!/usr/bin/env python
# coding: utf-8

# In[167]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 


#reading image and apply edges detection filter
img = cv.imread('redcell.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.medianBlur(gray, 5)

#detect circles in image
circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, img.shape[0]/11.5, param1=250, param2=10, minRadius=15, maxRadius=45)

if circles is not None:
    circles = np.uint16(np.around(circles))
    radius = []
    for i in range(0, len(circles[0, :])):
        radius.append(circles[0, :][i][2])
    print(radius)
    
#define white cells and redcells     
for i in circles[0, :]:
        # Draw bigger circles(white cells)
        if i[2] >42 :
            cv.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
        
        # Draw smaller circles(smaller cells)
        else:
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 255), 2)
      
      






cv.imshow('result', img)







cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




