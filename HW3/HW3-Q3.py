#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import math

img1 = cv.imread('clown.tif' , 0)
img2 = cv.imread('mandrill.tif' , 0)

#fft transform for image 1 : clown
dft1 = cv.dft(np.float32(img1),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift1 = np.fft.fftshift(dft1)

# magnitude spectrum and transform
mag1, phase1 = cv.cartToPolar(dft_shift1[:,:,0], dft_shift1[:,:,1])

cv.imshow('spercture1' , np.log(mag1)/20)
cv.imshow('phase1' , phase1)

#fft transform for image 2 : mandrill
dft2 = cv.dft(np.float32(img2),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift2 = np.fft.fftshift(dft2)

# magnitude spectrum and transform
mag2, phase2 = cv.cartToPolar(dft_shift2[:,:,0], dft_shift2[:,:,1])

cv.imshow('spercture2' , np.log(mag2)/20)
cv.imshow('phase2' , phase2)


# make new image from switching phases of two image that we have
real1, imag1 = cv.polarToCart(mag1, phase2)
back1 = cv.merge([real1, imag1])
back1_ishift = np.fft.ifftshift(back1)
img_back1 = cv.idft(back1_ishift)
img_back1 = cv.magnitude(img_back1[:,:,0], img_back1[:,:,1])

# re-normalize to 8-bits
img_back1 = cv.normalize(img_back1, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

# make new image from switching phases of two image that we have
real2, imag2 = cv.polarToCart(mag2, phase1)
back2 = cv.merge([real2, imag2])
back2_ishift = np.fft.ifftshift(back2)
img_back2 = cv.idft(back2_ishift)
img_back2 = cv.magnitude(img_back2[:,:,0], img_back2[:,:,1])

# re-normalize to 8-bits
img_back2 = cv.normalize(img_back2, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)


cv.imshow('clown' , img1)
cv.imshow('clown with new phase' , img_back1)
cv.imshow('mandrill' , img2)
cv.imshow('mandrill with new phase' , img_back2)

cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




