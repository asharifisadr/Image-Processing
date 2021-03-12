#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

def filtering(img,x):
# checkig that its array or string

    if isinstance(x , np.ndarray) :
        
        if x.shape[0]!=3 or x.shape[1]!=3 : 
            return False

        else :
        
            image = cv.copyMakeBorder(img, 1, 1, 1, 1, cv.BORDER_REFLECT101)

            for m in range(1 , image.shape[0]):
                for n in range(1 , image.shape[1]):
                    k = image[m,n]
                    for i in range(-1 , 1):
                        for j in range(-1 , 1):
                            image[m,n] = image [m,n] + (image[m+i,n+j]*x[i+1,j+1])
                            if i == 1 and j == 1 :
                                image[m,n] = image[m,n]-k
                                

        return image

    else :
        if x == 'median' :
            k = [0]*9


            image = cv.copyMakeBorder(img, 1, 1, 1, 1, cv.BORDER_REFLECT101)
            for m in range(1 , image.shape[0]-1):
                for n in range(1 , image.shape[1]-1):
                    k[0] = image[m-1,n-1]
                    k[1] = image[m-1,n]
                    k[2] = image[m-1,n+1]
                    k[3] = image[m,n-1]
                    k[4] = image[m,n]
                    k[5] = image[m,n+1]
                    k[6] = image[m+1,n-1]
                    k[7] = image[m+1,n]
                    k[8] = image[m+1,n+1]
                    k.sort(key=lambda x: x[0])
                    image[m,n] = k[4]
                    
            return image                   

                            
img = cv.imread('bone-scan.png')
cv.imshow('original' , img)
y = 'median'
cv.imshow('median' , filtering(img,y))

x = [[1/9]*3]*3
x = np.array(x)
cv.imshow('average' , filtering(img,x))





cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




