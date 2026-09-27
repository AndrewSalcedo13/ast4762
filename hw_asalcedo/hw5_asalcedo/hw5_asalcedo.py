#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#Homework 5: Sigma clip fitting
#9/27/2026


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from sigrej import *


# In[3]:


#Problem 2
#sample from practicum 3
CCD = np.array([])
CCD = np.append(CCD, np.random.poisson(10000,396))     #396 random poisson distributed values
CCD = np.append(CCD, np.random.uniform(0, 10**6, 4))   ##4 random unifrom distributed values
CCD_mean = np.mean(CCD)
CCD_med = np.median(CCD)
CCD_std = np.std(CCD)
print(f"CCD - \nmean: {CCD_mean}\nmedian: {CCD_med}\nstd: {CCD_std}\n")

#sub sample, clipped to be within 5 sigma of median from practicum 3
CCD_ss = CCD[ ( CCD_med - (5 * CCD_std) < CCD) & (CCD < CCD_med + (5 * CCD_std)) ]
CCD_ss_mean = np.mean(CCD_ss)
CCD_ss_med = np.median(CCD_ss)
CCD_ss_std = np.std(CCD_ss)
print(f"CCD subsample - \nmean: {CCD_ss_mean}\nmedian: {CCD_ss_med}\nstd: {CCD_ss_std}\n")

#sub sample of sub sample of CCD from practicum 3, clipped to be within 5 std of the median of CCD_ss
CCD_sss = CCD_ss[ (CCD_ss_med - (5 * CCD_ss_std) < CCD_ss) & (CCD_ss < (CCD_ss_med + (5 * CCD_ss_std)))]
CCD_sss_mean = np.mean(CCD_sss)
CCD_sss_med = np.median(CCD_sss)
CCD_sss_std = np.std(CCD_sss)
print(f"CCD sub-subsample - \nmean: {CCD_sss_mean}\nmedian: {CCD_sss_med}\nstd: {CCD_sss_std}\n")
#The final mean and median are very close after all the more extreme and outlier values have been clipped and the mean isnt being
#as affected by any extreme values.
#The std of a Poisson Distribution is given by the square root of N, in this case since N = 10000, the std of the poisson distribution
#should be around 100, since after the second clipping the std is 105 I would say that the std of the poisson distribution matches.
#This method of 'sigma clipping' will not always remove every bad pixel, only the most extreme ones that lie outside the determined std.


# In[11]:


#problem 3
CCD_mask = sigrej(CCD, (5, 5, 5))

CCD_clean_data = CCD[CCD_mask]
CCD_clean_data_mean = np.mean(CCD_clean_data)
CCD_clean_data_std = np.std(CCD_clean_data)
print(f"Cleaned data - \nmean: {CCD_clean_data_mean}\nstd: {CCD_clean_data_std}")
#The mean and std of the cleaned data set is equal to the one previously found, the function works


# In[ ]:




