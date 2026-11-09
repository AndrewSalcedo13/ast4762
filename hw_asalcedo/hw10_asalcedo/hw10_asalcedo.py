#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Andrew Salcedo
#HW 10: Photometry
#11/8/2026


# In[3]:


import numpy as np
from asalcedo_supp_funcs import*
from practicum7_asalcedo import*
from hw9_asalcedo import*
from gaussian import*


# In[4]:


print(photometry)
print(aper_r)
print(sky_in_rad)
print(sky_out_rad)
print(frames)


# In[9]:


#Problem 3: write a function do photometry
def dophot(phot_table, frames, pix_mask, apphot_r, annr_i, annr_o):
    '''
    does photometry on photometry table and fills in rest of values missing. Should run on each frame for each star
    '''
    for i in range(photometry.shape[0]):        #loop through each row(star)
        for j in range(photometry.shape[1]):    #loop through each column(frame)
            y_c = photometry[i, j, 3]           #3 and four contain the fitted coords for each star in each frame
            x_c = photometry[i, j, 4]

            #Uses apphot function to get stellar flux, aerage sky value and the bad pixels of each frame
            stllr_flx, avg_sky, bad_pix = apphot(
                frames[j],
                pix_mask,
                aper_r,
                sky_in_rad,
                sky_out_rad,
                (y_c, x_c))

            photometry[i, j, 5] = stllr_flx
            photometry[i, j, 6] = avg_sky
    return photometry

#running the function
pixel_mask = ~np.isnan(frames[0])
photometry = dophot(photometry, frames, pixel_mask, aper_r, sky_in_rad, sky_out_rad)
print(photometry)
#Its going to return an error because I still havent fixed the Nan values from homework 9 and my table is incorrect. 

#Below is how I would have saved my results to an ASCII file if I could get correct values
'''
with open('photometry.txt', 'w') as outfile:

    outfile.write("# Aperture Photometry Results\n")

    for i in range(photometry.shape[0]):

        outfile.write(f"\n# Star {i}\n")

        star_data = np.column_stack((
            np.arange(photometry.shape[1]),
            photometry[i]
        ))

        # Write the data to the file
        np.savetxt(
            outfile,
            star_data,
            fmt='%.8e',
            delimiter='\t',
            header='Frame y_approx x_approx width y_fit x_fit flux sky'
        )
'''


# In[ ]:




