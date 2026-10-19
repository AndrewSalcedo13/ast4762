#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#Homework 7: Fitting Data and Scientific Data Presentation
#10/9/2026


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
from window_function import*


# In[3]:


#Problem 3
#a) Read in data and make publication ready plot
data = pd.read_csv('hw7_synthetic_transit_lightcurve.csv')
print(data.head())
time = data['Time (days)']
Norm_flux = data['Normalized Flux']

plt.figure(figsize = (15,5))
plt.scatter(time, Norm_flux, color = 'b', s= 13, label = 'data')

ax = plt.gca()
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(4))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
plt.xticks(np.arange(-0.06, 0.07, 0.02))
plt.yticks(np.arange(0.988, 1.004, 0.002))
plt.tick_params(axis = 'both', which = 'major', length = 8, width = 1.5, direction = 'in')

plt.xlabel('Time (days)', fontsize = 16)
plt.ylabel('Normalized Flux', fontsize=16)
plt.title('Synthetic Transit Lightcurve', fontsize = 16)
plt.savefig('hw7_asalcedo_problem3a_graph1')


#b) 
#i) window function made and imported
from window_function import*
#ii) curve fit 
p0 = [0.0, 0.02, 0.99]                                  #center, width and height values
popt, pcov = curve_fit(window, time, Norm_flux, p0=p0)  #makes a fit for the flux, based on box params
cfit, wfit, hfit = popt                                 #finds best fit
print(f"Best-fit center: {cfit} days\nBest-fit width: {wfit} days\nBest-fit height: {hfit}")
#iii) best fit window function properties and planet radius
tran_depth = 1 - hfit
pla_radius = 1.14 * (1-hfit)**0.5
print(f"\nTransit Depth: {tran_depth}\nPlanet Radius: {pla_radius} R_sun")
#iv) plot
fit = window(time, *popt)
plt.plot(time, fit, color = 'r',label = 'best-fit')
plt.legend()
plt.savefig('hw7_asalcedo_problem3biv_graph1')
plt.show()


#c) planetary radius uncertainty
print(f"Planetary Radius error: 0.0115 R_sun")


# In[ ]:





# In[ ]:





# In[ ]:




