#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#practicum 7: Photometry
#11/08/26


# In[2]:


from asalcedo_supp_funcs import*
from gaussian import*
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


#problem 2: test apphot
#create gaussian image and apphot inputs
empty_img = np.indices((21,21))
gauss_img = gaussian(empty_img, 2, (10, 10), 1)
pix_mask = np.ones(gauss_img.shape, dtype = bool)     #noiseless image so every value is true

#run apphot on the guassian image
stllr_flux, avg_sky, bad_pix = apphot(gauss_img, pix_mask, 6, 7, 10, (10, 10))
print(f"The stellar flux of the image is: {stllr_flux}")
print(f"The average value of every pixel within the annulus is: {avg_sky}")
print(f"The number of bad pixels within the aperature is: {bad_pix}")


# In[ ]:





# In[ ]:




