#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
# reading original image     
img = cv.imread('C:/Users/Asus/Desktop/image/T.jpg',)
# showing original image     
cv.imshow('original image',img)
# performing scale operation on orginal image     
scale_img=cv.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv.INTER_LINEAR)
cv.imwrite('C:/Users/Asus/Desktop/image/scaling.jpg ',scale_img)
# making transformation function     
M = np.float32([[1,0,200],[0,1,100]])
# performing translate operation on original image      
translate_img = cv.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv.imwrite('C:/Users/Asus/Desktop/image/taranslation.jpg',translate_img)
# making transformation function    
M=np.float32([[1,0.5,0],[0,1,0]])
# performing vertical shear operation on original image    
vertical_shear_img = cv.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv.imwrite('C:/Users/Asus/Desktop/image/vertival shear.jpg',vertical_shear_img)
# making transformation function    
M=np.float32([[1,0,0],[0.5,1,0]])
# performing horizental shear operation on original image    
horizontal_shear_img = cv.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv.imwrite('C:/Users/Asus/Desktop/image/horizontal shear.jpg',horizontal_shear_img)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




