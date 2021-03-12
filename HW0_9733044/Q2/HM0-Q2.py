#!/usr/bin/env python
# coding: utf-8

# In[21]:


def prime(n):
    s=0
    for i in range(n):
        if n%(i+1)==0 :
            s+=1
    if s==2 :
        return("its a prime number")
    else:
        return("its not prime number")


n=4
print (n, prime(n)) #4 its not prime number


# In[ ]:





# In[ ]:




