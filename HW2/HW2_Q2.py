#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt


# intensity level slicing

def reduces_other_gray_level(x):
    if x>= 160 and x<=240 :
        return 150 
    else :
        return 20 

def preserves_other_gray_level(x):
    if x>=100 and x<=165 :
        return 200
    else :
        return x
    
img = cv.imread('kidney.tif')
cv.imshow('original image' , img)

vec = np.vectorize(reduces_other_gray_level)
img1 = vec(img)
img1 =  img1.astype('uint8')
cv.imshow('transformation with reduces other gray level' , img1)

vec = np.vectorize(preserves_other_gray_level)
img2 = vec(img)
img2 =  img2.astype('uint8')
cv.imshow('transformation with preserves other gray level' , img2)


cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




