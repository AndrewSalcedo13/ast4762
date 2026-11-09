#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#Practicum 5: Combining Frames and Infrared Sky Correction
#10/13/26


# In[14]:


import numpy as np
from astropy.io import fits
from asalcedo_supp_funcs import*
from hw6_asalcedo import*


# In[3]:


#problem 2: normmedcomb function
from asalcedo_supp_funcs import normmedcomb


# In[15]:


#problem3: call normmedcomb function on dark subtracted object data
normmedcomb(sub_obj_arr, ((225, 225),( -225, -225)))
norm_factors, master_flat = normmedcomb(sub_obj_arr, ((225, 225),( -225, -225)))
print(f"Normalization factors:\n{norm_factors}\n")
print(f"Master Flat:\n{master_flat}")

#Saving master flat to fits file, normalization factors stored in variable and printed
fits.writeto('sky_13s_mednorm.fits.', master_flat, overwrite=True)


# In[ ]:




