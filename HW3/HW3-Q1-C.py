#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import math 
img = cv.imread('chest.tif' ,0 )

# fft transform
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# magnitude spectrum and transform
mag, phase = cv.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])

# make new phase for doing mirror
phase=(-1)*phase

#making new real and imaginary of furier with new phase
real, imag = cv.polarToCart(mag, phase)

# mirror image around the center
mirror = cv.merge([real, imag])
mirror_ishift = np.fft.ifftshift(mirror)
img_mirror = cv.idft(mirror_ishift)
img_mirror = cv.magnitude(img_mirror[:,:,0], img_mirror[:,:,1])

# re-normalize to 8-bits
img_mirror = cv.normalize(img_mirror, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)


cv.imshow('original image' , img)
cv.imshow('mirror around the center' , img_mirror)







cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




