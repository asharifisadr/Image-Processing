#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import math 

# power law function
def power_law(img,gamma):
    
    img_power_law_transformation = np.array(255*(img / 255) ** gamma , dtype = 'uint8') 
    return img_power_law_transformation

# logarithm transform function 
def log_transform(img,k):
    
    c = 255/(math.log(1 + np.max(img),k)) 
   
    img_log_transformation = c * (np.log(1 + img )/ np.log(k))
    img_log_transformation = np.array(img_log_transformation, dtype = 'uint8') 
   
    return img_log_transformation


# reading image and showing after power law effect with gamma = 1.2
img = cv.imread('brains.png',)
cv.imshow('power law' , power_law(img,1.2))

# finding suitable amount for gamma
gamma=0.6
a = power_law(img,gamma)

# making 2*3 plot
fig , ax = plt.subplots(2,3,figsize=(10,10))
fig.suptitle('contrast improvement')

# drawing wanted plot 
ax = plt.subplot(2,3,1)
ax.imshow(a, cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('power law transformation')

ax = plt.subplot(2,3,4)
ax.hist(a.ravel() , bins = 256 )
ax.axes.get_yaxis().set_visible(False)

# apply logarithm transform 
k = 5
b = log_transform(img,k)
         
ax = plt.subplot(2,3,2)
ax.imshow(b, cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('log transformation')

ax = plt.subplot(2,3,5)
ax.hist(b.ravel() , bins = 256 )
ax.axes.get_yaxis().set_visible(False)

ax = plt.subplot(2,3,3)
ax.imshow(img, cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('original image')

ax = plt.subplot(2,3,6)
ax.hist(b.ravel() , bins = 256 )
ax.axes.get_yaxis().set_visible(False)


cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




