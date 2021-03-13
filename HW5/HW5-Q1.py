#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math 

# reading image and defining points function 
def points(img_name,qoordinates):
    img = cv.imread(img_name)
    cv.imshow('image',img)
# select points with click    
    def click_event(event, x, y, flags, params):
        
        if event == cv.EVENT_LBUTTONDOWN: 
            print(x,y)
            qoordinates.append((x,y))
           
            
          

            font = cv.FONT_HERSHEY_SIMPLEX 
            cv.putText(img, str(x) + ',' + str(y), (x,y), font, 0.25, (255, 0, 0), 1) 
            cv.imshow('image', img)
    
#selecting poitn while we press "space" key                                
    while 1:
        cv.setMouseCallback('image', click_event) 
        key = cv.waitKey(0) 
        if key == 32:
            break


print('three points of image 1 ')
qoordinates1 = []
points('MRIF.png' ,qoordinates1 )
#making array of points with float32 type 
qoordinates1 = np.array(qoordinates1 , dtype='float32')

print('three points of image 2')
qoordinates2 = []
points('MRIS.png',qoordinates2)
#making array of points with float32 type
qoordinates2 = np.array(qoordinates2 , dtype='float32')
  
#calculate transform function
Affine = cv.getAffineTransform(qoordinates2, qoordinates1)
print(Affine)

#Apply the transform function on the image
img = cv.imread('MRIS.png')
affine_transform_image= cv.warpAffine(img, Affine, (1000, 1000))
cv.imshow('new image', affine_transform_image)
cv.waitKey(0)


cv.destroyAllWindows()



# In[ ]:





# In[ ]:




