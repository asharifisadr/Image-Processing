#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 

img=cv.imread('noisy_rectangle.png' , 0) 

#A
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))

erosion = cv.erode(img,kernel,iterations = 1)

dilation = cv.dilate(img,kernel,iterations = 1)


#B 
kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (36, 47))

#erosion1 = cv.erode(img,kernel1,iterations = 1)
#dilation1 = cv.dilate(erosion1,kernel1,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel1)

# C 
kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (29, 32))

#dilation2 = cv.dilate(opening,kernel2,iterations = 1)
#erosion2 = cv.erode(dilation2,kernel2,iterations = 1)
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel2)


plt.figure(figsize=(20,20))

plt.subplot(2,2,1)
plt.title('Erosion')
plt.imshow(erosion , cmap= 'gray' , vmin = 0 , vmax = 255)

plt.subplot(2,2,2)
plt.title('Dilation')
plt.imshow(dilation , cmap = 'gray' , vmin = 0 , vmax = 255)

plt.subplot(2,2,3)
plt.title('Opening')
plt.imshow(opening , cmap = 'gray' , vmin = 0 , vmax = 255)

plt.subplot(2,2,4)
plt.title('Closing')
plt.imshow(closing , cmap = 'gray' , vmin = 0 , vmax = 255)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




