#!/usr/bin/env python
# coding: utf-8

# In[75]:


from tools import*
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 
from skimage import restoration
from skimage.restoration import wiener

retina = cv.imread('retina_motionblurred.jpg',0)
retina1 = cv.imread('retina.jpg',0)


# A 
kernel = np.eye(13,13)
kernel = kernel /13  

# B 
# input: 2D image, output: float 2D image in range [-1, 1] 
img = normal(retina)
# Applying wiener function in motionblurred image to make it better 
deconvolution_img = wiener(img , kernel , 0.06)

# input: 2D image, output: uint8 2D image in range [0, 255]
restored = n_range(deconvolution_img)

# C 
plt.figure(figsize=(10,10)) 
plt.subplot(2,2,1)
plt.imshow(retina , cmap='gray' , vmin = 0 , vmax = 255 )

plt.subplot(2,2,2)
plt.imshow(restored , cmap='gray' , vmin = 0 , vmax = 255 )

plt.subplot(2,2,3)
plt.imshow(logmagnitude(retina) , cmap='gray' )

plt.subplot(2,2,4)
plt.imshow(logmagnitude(restored) , cmap='gray' )




plt.show()
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




