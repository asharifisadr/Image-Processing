#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
# reading original image and mask image
img = cv.imread('C:/Users/Asus/Desktop/image/dental_xray.tif',)
img_mask = cv.imread('C:/Users/Asus/Desktop/image/dental_xray_mask.tif',)
# making new space for result image 
new_img = np.zeros(img.shape, img.dtype)
# separating marked section im mask image from orginal image and put them in new image      
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if all(img_mask[i,j] == (255,255,255)): 
            new_img[i,j]=img[i,j].copy()
# showing result 
cv.imshow('new_image',new_img)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




