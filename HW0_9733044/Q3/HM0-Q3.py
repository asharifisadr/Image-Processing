#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
from matplotlib import pyplot as plt

def mapping(arr):
    arr=(((arr-arr.min())/(arr.max()-arr.min()))*255) # mapping operation 
    arr = arr.astype('uint8') # changing data type to int
    return arr

rnd = np.random.uniform(-3.2, 9.3, size=(50, 40,3)) # making 3d array and filling it with random number from [-3.2,9.2]
print('array befor transform:\n', rnd) 
print('\n')
print('Min of array: ' , rnd.min(), 'Max of array: ', rnd.max())
print('\n')
print('Array after transform:\n', mapping(rnd))
a = mapping(rnd) # Apply the function to the specified array
plt.imshow(np.array(a)) # function for imaging array
plt.show() # show image 


# In[ ]:





# In[ ]:




