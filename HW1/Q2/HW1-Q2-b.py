#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
# reading image as gray color 
img_gray = cv.imread('C:/Users/Asus/Desktop/image/partial_body_scan.tif',0)
# BGR TO RGB transfrom for showing in plot 
img_gray=cv.cvtColor(img_gray,cv.COLOR_BGR2RGB)
# making image matrix for complement image 
img_complement = np.zeros(img_gray.shape, img_gray.dtype)

# filling maked matrix 
for i in range(img_gray.shape[0]):
    for j in range(img_gray.shape[1]):
        img_complement[i,j] = 255 - img_gray[i,j]

# union of gary image and gray image's complemet 

img_combine = cv.add(img_gray,img_complement)

# making subplot for showing images that maked 
plt.figure(figsize=(10,10)) 
plt.subplot(1,3,1)    
plt.imshow(img_gray)
plt.subplot(1,3,2)    
plt.imshow(img_complement)
plt.subplot(1,3,3)    
plt.imshow(img_combine)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




