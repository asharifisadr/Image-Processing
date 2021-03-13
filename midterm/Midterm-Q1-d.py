#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 


def bit_plane_slicing(img,bit):
    bit_image = np.zeros(img.shape , dtype = 'uint8')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            b = np.binary_repr(img[i,j],width=8)
            bit_image[i,j]=b[7-bit]
    return bit_image

img = cv.imread('retina.jpg',0)

plt.figure(figsize=(20,20)) 
plt.subplot(2,4,1)
plt.title('8th bit - most valuable')
plt.imshow(bit_plane_slicing(img,7) , cmap='gray' )    
plt.subplot(2,4,2)
plt.title('7th bit')
plt.imshow(bit_plane_slicing(img,6), cmap='gray')    
plt.subplot(2,4,3)
plt.title('6th bit')
plt.imshow(bit_plane_slicing(img,5), cmap='gray')    
plt.subplot(2,4,4)
plt.title('5th bit')
plt.imshow(bit_plane_slicing(img,4), cmap='gray')    
plt.subplot(2,4,5)
plt.title('4th bit')
plt.imshow(bit_plane_slicing(img,3), cmap='gray')    
plt.subplot(2,4,6)
plt.title('3th bit')
plt.imshow(bit_plane_slicing(img,2), cmap='gray')    
plt.subplot(2,4,7)
plt.title('2th bit')
plt.imshow(bit_plane_slicing(img,1), cmap='gray')    
plt.subplot(2,4,8)
plt.title('1th bit - less valuable')
plt.imshow(bit_plane_slicing(img,0), cmap='gray')    

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




