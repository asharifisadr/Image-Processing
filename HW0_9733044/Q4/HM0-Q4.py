#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np


def derivative(coef): #  Calculate coefficients derived from polynomial coefficients
    dcoef = np.arange(len(coef)-1)
    for i in range(1,len(coef)):
        dcoef[i-1]=coef[i]*i 
    return dcoef # coefficints of derivative  

def poly(x,coef): # Construct polynomials using existing coefficients
    y = 0
    for i in range(len(coef)):
        y+=coef[i]*(x**i)
    return y 

coef=[1,2,3,4,0,6,7]  # Input coefficients
print('derivative coefficients  ',derivative(coef)) # print derivative coefficients
dcoef = derivative(coef)
x = np.linspace(-100,100, 1000000) # custom range
plt.plot(x, poly(x,coef),linestyle='-',color='b',label='polynomial')
plt.plot(x, poly(x,dcoef),linestyle='--',color='r',label='first polynomial derivation')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('PLOT')
plt.legend(loc='lower right')
plt.axis([-10,10,-10,20])
plt.show()


# In[179]:





# In[ ]:





# In[ ]:




