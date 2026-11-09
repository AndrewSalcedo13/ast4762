#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#practicum 6: Combining Frames and Data image analysis
#10/22/26


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from asalcedo_supp_funcs import*
from hw6_data import*
from practicum5_asalcedo import*
from hw6_asalcedo import*
from hw7_asalcedo import*
from hw8_asalcedo import*


# In[23]:


#Problem 1: write disk function and test it on, store results in a fits file and print [14, 14] and [2, 1]
disktest = disk(6.2, (12.3, 14.5), (25, 30))
fits.writeto('disktest.fits', disktest.astype(np.uint8), overwrite = True)
plt.imshow(disktest)
print(f"values\n[14, 14]: {disktest[14, 14]}\n[2, 1]: {disktest[2, 1]}")


# In[4]:


#Read in k_lampon and k_lampoff data
k_lampon = filefind('hw6_data/', '.fits', 'k_lampon', load_data = True)
k_lampoff = filefind('hw6_data/', '.fits', 'k_lampoff', load_data = True)


# In[21]:


#Problem 2
#a)
#create flat-field frame for k_lampon and k_lampoff data(using median combination)
lon_f = medcomb(k_lampon[1])
loff_f = medcomb(k_lampoff[1])

#subtracting median combined lampoff flat from lampon flat
sub_lon_f = lon_f - loff_f

#Normalizing region according to region ((225, 225),( -225, -225))
norm_lon_flat = normmedcomb(k_lampon[1], ((225, 225),(-225, -225)))
norm_lon_flat = norm_lon_flat[1]  #gives us the master flat not the normalization factors

#now normalize previous median combine result accoridng to same region
k_lampon_flat = skycormednorm(sub_lon_f, norm_lon_flat, ((225, 225),(-225, -225)))
fits.writeto('flat.fits', k_lampon_flat, overwrite = True)
print(k_lampon_flat[217, 184])

#b) Apply k_lampon_flat to all skysubtracted data(from hw8)
skysub = np.array(sky_sub)
stars = np.zeros(skysub.shape, dtype=np.float64)
stars_val = []

for i in range(skysub.shape[0]):
    stars[i] = sky_sub[i]
    stars[i] /= k_lampon_flat
    stars_val.append(stars[i, 217, 184])

#writing last frame to fits file with modified header and printing values of each frame
fits.writeto('stars_13s_9_flat.fits', stars[-1], overwrite=True)
print(stars_val)


# In[ ]:





# In[ ]:




