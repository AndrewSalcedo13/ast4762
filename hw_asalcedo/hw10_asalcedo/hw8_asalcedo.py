#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#Homework 8: Array Corrections
#10/18/2026


# In[2]:


import numpy as np
from hw6_asalcedo import*
from hw7_asalcedo import*
from practicum5_asalcedo import*
from asalcedo_supp_funcs import*


# In[18]:


#2

sky_sub = []
for i in range (sub_obj_arr.shape[0]):
    sub_obj_frame = sub_obj_arr[i]
    sky_sub_frame = skycormednorm(sub_obj_frame, master_flat)
    sky_sub.append(sky_sub_frame)

fits.writeto('stars_13s_9_nosky.fits', sky_sub[-1], overwrite = True)

print(sky_sub[-1][217][184])


# In[ ]:





# In[ ]:





# In[ ]:




