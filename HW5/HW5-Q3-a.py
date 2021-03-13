#!/usr/bin/env python
# coding: utf-8

# In[171]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 

#reading image and apply edges detection filter
img = cv.imread('surgery.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.medianBlur(gray,11)
edges = cv.Canny(img_blur, 50, 100)
#cv.imshow('image' , edges)

#detect line in image
lines = cv.HoughLinesP(edges, 1, np.pi/180 , 50, minLineLength=30 , maxLineGap=10)

# Draw lines on the image
for line in lines:

    x1, y1, x2, y2 = line[0]

    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

# Show result
cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




