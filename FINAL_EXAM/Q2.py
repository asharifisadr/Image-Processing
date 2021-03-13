#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt



def filling_hole(img_name):
    global img 
    img = cv.imread(img_name,0)
    img1 = cv.imread(img_name,0)
    img1 = cv.threshold(img1,20,255,cv.THRESH_BINARY)[1]
    img1 = 255 - img1 
    
    cv.imshow('image',img)
# select points with click    
    def click_event(event, x, y, flags, params):
        global img 
        img2 = np.zeros(img.shape ,dtype='uint8')
        kernel = cv.getStructuringElement(cv.MORPH_CROSS,(3, 3))
        k = 0
        
        if event == cv.EVENT_LBUTTONDOWN: 
            img2[y,x]=255
                
            while (k==0):
                
                img3 = img2
                img2 = cv.dilate(img2,kernel,iterations = 1 )
                #for i in range(img2.shape[0]):
                    #for j in range(img2.shape[1]):
                        #if (img2[i,j]!=img1[i,j]):
                            #img2[i,j]=0
                img2 = cv.bitwise_and(img2, img1)
                          
                if np.all(img2==img3):
                    k=1
                    #for i in range(img2.shape[0]):
                        #for j in range(img2.shape[1]):
                            #if (img2[i,j]==255):
                                #img[i,j]=img2[i,j]
                    img = cv.bitwise_or(img2, img)
                    cv.imshow('image', img)
    
#selecting poitn while we press "esc" key                                
    while 1:
        cv.setMouseCallback('image', click_event) 
        key = cv.waitKey(0) 
        if key == 27:
            cv.destroyAllWindows()
            break


filling_hole('reflections.jpg')
            
            
            

cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




