#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 

def transform(img):
    l = 256
    a = math.pi/(2*(l-1)) 
    transform_img = (l-1)*(np.sin(a*img))
    transform_img = np.round_(transform_img)
    transform_img = np.array(transform_img , dtype = 'uint8')
    return transform_img

img1 = cv.imread('CT_1.tif',0)
img2 = cv.imread('CT_2.tif',0)

fig , ax = plt.subplots(2,2,figsize=(10,10))
fig.suptitle('contrast improvement')

# show original image 
ax = plt.subplot(2,2,1)
ax.imshow(img1, cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('original image1')

# show original image 
ax = plt.subplot(2,2,3)
ax.imshow(img2, cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('original image2')

# show image after transform function
ax = plt.subplot(2,2,2)
ax.imshow(transform(img1), cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('transform image1')

# show image after transform function
ax = plt.subplot(2,2,4)
ax.imshow(transform(img2), cmap = 'gray', vmin=0 , vmax=255)
ax.axis('off')
ax.set_title('transform image2')


fig , ax = plt.subplots(1,1,figsize=(10,10))
fig.suptitle('plot')

l = 256
x = np.arange(l)
y = transform(x)

# plotting transform curve
ax.plot(x,y,color='b' ,label='transform curve' )

# plotting identity function
ax.plot(x , color='r' ,label = 'identity')

ax.legend(loc='lower right')
plt.axis([0,l-1,0,l-1])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()




# In[ ]:





# In[ ]:




