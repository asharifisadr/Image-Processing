#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import math 
img = cv.imread('chest.tif' ,0 )

# FFT TRANSFORM
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# MAGNITUDE SPERCTRUM AND PHASE
mag, phase = cv.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])
spectrum = np.log(mag)/20


# SHIFTING BACK CENTER
back_ishift = np.fft.ifftshift(dft_shift)

# USE INVERSE FFT TO GET IMAGE BACK
img_back = cv.idft(back_ishift)
img_back = cv.magnitude(img_back[:,:,0], img_back[:,:,1])
img_back = cv.normalize(img_back, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)


cv.imshow("ORIGINAL", img)
cv.imshow("PHASE", phase)
cv.imshow("SPECTRUM", spectrum)
cv.imshow("INVERSE", img_back)



cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




