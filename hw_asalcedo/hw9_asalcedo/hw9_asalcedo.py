#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Andrew Salcedo
#Homework 9: Photometry Setup
#10/25/2026


# In[31]:


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from asalcedo_supp_funcs import*
from gaussian import*
from hw6_data import*
from practicum5_asalcedo import*
from practicum6_asalcedo import*
from hw6_asalcedo import*
from hw7_asalcedo import*
from hw8_asalcedo import*


# In[82]:


#problem 2
photometry = np.array( [ # yguess, xguess, width, cy, cx, star, sky
# star 0
[ [ 850, 775, np.nan, np.nan, np.nan, np.nan, np.nan], # frame 0
[ 999, 999, np.nan, np.nan, np.nan, np.nan, np.nan],   # frame 1
[ 999, 999, np.nan, np.nan, np.nan, np.nan, np.nan]],  # frame 2
# star 1
[ [ 970, 970, np.nan, np.nan, np.nan, np.nan, np.nan],     # frame 0
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 1
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], # frame 2
# star 2
[ [ 780, 780, np.nan, np.nan, np.nan, np.nan, np.nan],     # frame 0
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # frame 1
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]  # frame 2
], dtype=float)

#calculating offset of star 0 between frames 0 and 1, and 0 and 2
offset0_f1_0y = photometry[0, 1, 0] - photometry[0, 0, 0]
offset0_f1_0x = photometry[0, 1, 1] - photometry[0, 0, 1]
offset0_f2_0y = photometry[0, 2, 0] - photometry[0, 0, 0]
offset0_f2_0x = photometry[0, 2, 1] - photometry[0, 0, 1]

#add offset to stars position for stars 1 and 2 frame 0, append to table
nstars = photometry.shape[0]
nframes = photometry.shape[1]
for i in range(nstars):
    # Frame 1
    photometry[i, 1, 0] = photometry[i, 0, 0] + offset0_f1_0y
    photometry[i, 1, 1] = photometry[i, 0, 1] + offset0_f1_0x

    # Frame 2
    photometry[i, 2, 0] = photometry[i, 0, 0] + offset0_f2_0y
    photometry[i, 2, 1] = photometry[i, 0, 1] + offset0_f2_0x


# In[89]:


#load in data for 3 frames
frame1 = filefind('hw6_data/', '.fits', 'stars_13s_1', load_data = True)[1].squeeze()
frame2 = filefind('hw6_data/', '.fits', 'stars_13s_2', load_data = True)[1].squeeze()
frame3 = filefind('hw6_data/', '.fits', 'stars_13s_3', load_data = True)[1].squeeze()
frames = np.array([frame1, frame2, frame3])


# In[90]:


#Problem 3
#a)
half_size = 8

for s in range(nstars):          # Three stars
    for f in range(nframes):      # Three frames

        # Approximate position from your table
        yguess = photometry[s, f, 0]
        xguess = photometry[s, f, 1]

        # Extract a 17 x 17 subimage around the star
        ystart = int(yguess - half_size)
        yend = int(yguess + half_size + 1)
        xstart = int(xguess - half_size)
        xend = int(xguess + half_size + 1)

        subimage = frames[f, ystart:yend, xstart:xend].copy()
        if subimage.size == 0:
            print(f"Empty subimage: frame {f}, star {s}")
            continue

        # Subtract the median background
        subimage -= np.nanmedian(subimage)

        # Initial guesses for the Gaussian
        guess = (
            (2., 2.),  # Width in y and x, in pixels
            (yguess - ystart, xguess - xstart),  # Center in subimage
            np.nanmax(subimage)  # Peak height
        )

        # Fit the Gaussian to the pixel data
        width, center, height, err = fitgaussian(
            subimage,
            guess=guess
        )

        # Save fitted values in the table
        photometry[s, f, 2] = np.mean(width)
        photometry[s, f, 3] = center[0] + ystart
        photometry[s, f, 4] = center[1] + xstart

print(photometry)

#b) avg all widths and apply to whole dataset
# Average fitted Gaussian width across all stars and frames
avg_width = np.mean(photometry[:, :, 2])


# Photometry aperture radius
aper_r = 3 * avg_width

# Inner and outer sky-annulus radii
sky_in_rad = 4 * avg_width
sky_out_rad = 6 * avg_width

# Width of the square subimage used for photometry
subimage_size = 12 * avg_width


# In[ ]:





# In[ ]:




