#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 

plt.figure(figsize=(10,10))

# A
img1 = cv.imread('fingerprint.png' , 0 )
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
opening = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
plt.subplot(2,2,1)
plt.title('denoised image')
plt.imshow(closing , cmap = 'gray' , vmin = 0 , vmax = 255)

# B
img2 = cv.imread('headCT.png' , 0 )
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
gradient = cv.morphologyEx(img2, cv.MORPH_GRADIENT, kernel)
plt.subplot(2,2,2)
plt.title('gradient 3')
plt.imshow(gradient , cmap = 'gray', vmin = 0 , vmax = 255)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
gradient = cv.morphologyEx(img2, cv.MORPH_GRADIENT, kernel)
plt.subplot(2,2,3)
plt.title('gradient 7')
plt.imshow( gradient , cmap = 'gray' , vmin = 0 , vmax = 255)

# C 
img3 = cv.imread('rice.tif', 0)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (80, 80))
tophat = cv.morphologyEx(img3, cv.MORPH_TOPHAT, kernel)
ret, thresh = cv.threshold(tophat, 55, 255, cv.THRESH_BINARY)
plt.subplot(2,2,4)
plt.title('rice extraction')
plt.imshow(thresh , cmap = 'gray' , vmin = 0 , vmax = 255)



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()



# In[ ]:





# In[ ]:




