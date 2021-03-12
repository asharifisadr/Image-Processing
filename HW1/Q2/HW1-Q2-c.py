#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
# reaidng image     
img_live = cv.imread('C:/Users/Asus/Desktop/image/angiography_live.tif',)
img_mask = cv.imread('C:/Users/Asus/Desktop/image/angiography_mask.tif',)
# making new image from diffrence of "live image" and "mask image"     
img_diff = cv.absdiff(img_live, img_mask)
# making complement of diff image     
for i in range(img_live.shape[0]):
    for j in range(img_live.shape[1]):
        img_diff[i,j]=255-img_diff[i,j]
# showing complement image     
cv.imshow('image maked by diffrence',img_diff)
# normalizing complement image     
cv.normalize(img_diff, img_diff, 0, 255, cv.NORM_MINMAX)
# showing the normalize image     
cv.imshow('new image after normalize',img_diff)  
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




