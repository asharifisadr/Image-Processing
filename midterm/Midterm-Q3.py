#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import matplotlib.pyplot as plt
import cv2

# must be read in "gray" mode 
img = cv2.imread('lung.png',0)

# the best filter for slat and paper noise is median and its nonlinear
img_2 = cv2.medianBlur(img, 3)

# for vertical gradiant 
img_3= cv2.Sobel(img_2,cv2.CV_64F,dx=0,dy=1)

plt.figure()
plt.suptitle('Problem 3 Figure')

plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')
plt.axis(False)

plt.subplot(1, 3, 2)
plt.title('Denoised')
plt.imshow(img_2, cmap='gray')
plt.axis(False)

plt.subplot(1, 3, 3)
plt.title('Gradient')
plt.imshow(img_3, cmap='gray')
plt.axis(False)

plt.show()



# In[ ]:




