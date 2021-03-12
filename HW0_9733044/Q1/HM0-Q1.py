#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
import math 
a , b = -3 , 4  # numbers Interval of integration [a,b)
h = 0.005 # step
s = 0 # sum
for x in np.arange(a+h, b, h):
      s+=2*math.sin(x*x)

s+=math.sin(a*a)
t=(s*h)/2 # t is result of integral by  Trapezoidal rule 
print('result of integral by  Trapezoidal rule  ',t) 


# In[ ]:





# In[ ]:




