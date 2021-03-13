#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# four neighbor 
def region_growing_4neighbor(img_name):
    global img 
    img = cv.imread(img_name,0)

    cv.imshow('image',img)

    img = np.int64(img)
    
    global img_seg
    img_seg=np.zeros_like(img)
        
# select seed with click    
    def click_event(event, x, y, flags, params):
        global img 
        global img_seg
   
        if event == cv.EVENT_LBUTTONDOWN: 
            k = 0 
            img_seg[y,x] = 255 
            seed = img[y,x]
            img3 = np.zeros_like(img)

            while (k==0):
                img3 = img_seg.copy()
                
                for i in range(0,img.shape[0]):
                    for j in range(0,img.shape[1]):
                        
                        if(img_seg[i,j] == 255) :
                            
                            if (abs(img[i - 1, j] - seed) < 11 ) :
                                img_seg[i - 1,j] = 255
                            
                            if (abs(img[i  , j - 1] - seed) < 11 ) :
                                img_seg[i,j - 1] = 255
                            
                            if (abs(img[i + 1 , j] - seed) < 11  ):
                                img_seg[i + 1,j] = 255
                            
                            if (abs(img[i , j + 1] - seed) < 11 ):
                                img_seg[i,j + 1] = 255
                                                        

                if np.all(img_seg==img3):
                    k=1
                    img_seg = img_seg.astype(np.uint8)
                    cv.imshow('4 - region growing' , img_seg)
                    cv.imwrite('out4.png' , img_seg)
#selecting seed while we press "esc" key                                
    while 1:
        cv.setMouseCallback('image', click_event) 
        key = cv.waitKey(0) 
        if key == 27:
            cv.destroyAllWindows()
            break

############################

# eight neighbor
def region_growing_8neighbor(img_name):
    
    global img 
    img = cv.imread(img_name,0)
    
    cv.imshow('image',img)

    img = np.int64(img)
    global img_seg
    img_seg=np.zeros_like(img)
        
# select seed with click    
    def click_event(event, x, y, flags, params):
        global img 
        global img_seg
   
        if event == cv.EVENT_LBUTTONDOWN: 
            k = 0 
            img_seg[y,x] = 255 
            seed = img[y,x]
            img3 = np.zeros_like(img)

            while (k==0):
                img3 = img_seg.copy()
                
                for i in range(0,img.shape[0]):
                    for j in range(0,img.shape[1]):
                        
                        if(img_seg[i,j] == 255) :
                            
                            if (abs(img[i - 1, j] - seed) < 11 ) :
                                img_seg[i - 1,j] = 255
                            
                            if (abs(img[i  , j - 1] - seed) < 11 ) :
                                img_seg[i,j - 1] = 255
                            
                            if (abs(img[i + 1 , j] - seed) < 11  ):
                                img_seg[i + 1,j] = 255
                            
                            if (abs(img[i , j + 1] - seed) < 11 ):
                                img_seg[i,j + 1] = 255
                            
                            if (abs(img[i + 1, j+1] - seed) < 11 ) :
                                img_seg[i + 1,j+1] = 255
                            
                            if (abs(img[i - 1 ,j - 1] - seed) < 11 ) :
                                img_seg[i - 1 ,j - 1] = 255
                            
                            if (abs(img[i + 1 , j - 1] - seed) < 11  ):
                                img_seg[i + 1, j - 1 ] = 255
                            
                            if (abs(img[i -1 , j + 1] - seed) < 11 ):
                                img_seg[i -1 ,j + 1] = 255
                                                        

                if np.all(img_seg==img3):
                    k=1
                    img_seg = img_seg.astype(np.uint8)
                    cv.imshow('8 - region growing' , img_seg)
                    cv.imwrite('out8.png' , img_seg)
#selecting seed while we press "esc" key                                
    while 1:
        cv.setMouseCallback('image', click_event) 
        key = cv.waitKey(0) 
        if key == 27:
            cv.destroyAllWindows()
            break

            
b = False            
            
if b == True :           
    region_growing_4neighbor('fMRI.jpg')
else :
    region_growing_8neighbor('fMRI.jpg')


cv.waitKey(0)
cv.destroyAllWindows()


# 
