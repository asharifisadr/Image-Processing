#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#reading imafe from path
img = cv.imread('c:/Users/Asus/Desktop/image/mandrill.jpg',)
#part a of question that wants image's shape and data tpye of pixels
print(img.shape)
print(img)
width=img.shape[1]
width_cutoff=width//2
#part b of question : making image's color gray 
img_gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imwrite('c:/Users/Asus/Desktop/image/img_gray.jpg', img_gray)
#part c of question : transform brightness level of image from 256 t0 64,16,2
img1=(img/255)*64
img1 = img1.astype('uint8')
img2=(img/255)*16
img2 = img2.astype('uint8')
img3=(img/255)*2
img3 = img3.astype('uint8')
cv.imwrite('c:/Users/Asus/Desktop/image/img64.jpg', img1)
cv.imwrite('c:/Users/Asus/Desktop/image/img16.jpg', img2)
cv.imwrite('c:/Users/Asus/Desktop/image/img2.jpg', img3) 
#part d of question : devide image into two equal parts
crop1=img[: ,  :width_cutoff]
cv.imwrite('c:/Users/Asus/Desktop/image/lefo of crop.jpg',crop1)
crop1=cv.cvtColor(crop1,cv.COLOR_BGR2RGB)
crop2=img[:,  width_cutoff: ]
cv.imwrite('c:/Users/Asus/Desktop/image/right of crop.jpg',crop2)
crop2=cv.cvtColor(crop2,cv.COLOR_BGR2RGB)
#show those two crop parts in one plot with using subplot 
plt.figure(figsize=(8,8)) 
plt.subplot(1,2,1)    
plt.imshow(crop1)
plt.subplot(1,2,2)    
plt.imshow(crop2)
plt.show()
#part e of question : flip image from right to left and bottom to top 
img_inverse_rtl=img[::, ::-1].copy()
cv.imwrite('c:/Users/Asus/Desktop/image/right to left inverse.jpg ',img_inverse_rtl)
img_inverse_btt=img[::-1, ::].copy()
cv.imwrite('c:/Users/Asus/Desktop/image/bottom to top inverse.jpg ',img_inverse_btt)
img_inverse_btt=cv.cvtColor(img_inverse_btt,cv.COLOR_RGB2GRAY)
#part f of question : save fliped image with gary color in spicify path 
cv.imwrite('c:/Users/Asus/Desktop/image/gray flip.png',img_inverse_btt)
# part g of question : resize gary image with bilinear, nearest neighbor and duplicate pixels methods 
img_stretch1=cv.resize(img_gray,(0,0),fx=3,fy=3,interpolation=cv.INTER_LINEAR)
cv.imwrite('c:/Users/Asus/Desktop/image/img_stretch1.jpg',img_stretch1)
img_withdraw1=cv.resize(img_gray,(0,0),fx=1/3,fy=1/3,interpolation=cv.INTER_LINEAR)
cv.imwrite('c:/Users/Asus/Desktop/image/img_withdraw1.jpg',img_withdraw1)
img_stretch2=cv.resize(img_gray,(0,0),fx=3,fy=3,interpolation=cv.INTER_NEAREST)
cv.imshow('img_stretch2',img_stretch2)
img_withdraw2=cv.resize(img_gray,(0,0),fx=1/3,fy=1/3,interpolation=cv.INTER_NEAREST)
cv.imshow('img_withdraw2',img_withdraw2)
img_stretch3=cv.resize(img_gray,(0,0),fx=3,fy=3,interpolation=cv.INTER_AREA)
cv.imshow('img_stretch3',img_stretch3)
img_withdraw3=cv.resize(img_gray,(0,0),fx=1/3,fy=1/3,interpolation=cv.INTER_AREA)
cv.imshow('img_withdraw3',img_withdraw3)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




