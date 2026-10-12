#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#Practicum 4: Reading and Managing Imaging Data
#10/01/2026


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits


# In[3]:


#Problem 2

#   part a) two variables holding only the directory name and extension name, as strings
#variables are strings and do not access the files
datadir = "hw6_data/"
fext = ".fits"

#   part b) two lists one for target images and one for dark. lists populated with relevant files, using os command
objfile = []
for i in os.listdir(datadir):
    if "stars_13s_" in i:
        objfile.append(i.replace(fext, ""))
darkfile = []
for i in os.listdir(datadir):
    if "dark_13s_" in i:
        darkfile.append(i.replace(fext, ""))

#   part c) informative statements
print(f"\nData Directory: {datadir}")
print(f"Extension: {fext}")
print(f"Last element in object file: {objfile[-1]}")
print(f"Last element in dark file: {darkfile[-1]}\n")

#   part d) read any object file and determine data array sizes assign variables(nx, ny)
ny, nx = fits.getdata(datadir + objfile[0] + fext).shape

#part e) variables containing number of files in objfile and darkfile, also informative statements
nobj = len(objfile)
ndark = len(darkfile)
#Not hardcoded in case number of files in datadir changes
print(f"Number of rows in the first object file image: {ny}")
print(f"Number of elements/colummns in row 1 of the first object file: {nx}")
print(f"Number of Dark files: {ndark}")
print(f"Number of Object files: {nobj}\n")


# In[4]:


#problem 3

#part a) two 3d arrays one for objfile and one for darkfile, print shape
obj_arr = np.float64(np.zeros((nobj, ny, nx)))
print(f"Shape of Object array: {obj_arr.shape}")
dark_arr = np.float64(np.zeros((ndark, ny, nx)))
print(f"Shape of Dark array: {dark_arr.shape}\n")

#part b) read obj and dark data into cubes, save last header from each set in variable
for i in range(nobj):      #populating object array
    obj_arr[i] = fits.getdata(datadir + objfile[i] + fext)
    objhead = fits.getheader(datadir + objfile[i] + fext)

for i in range(ndark):     #populating dark array
    dark_arr[i] = fits.getdata(datadir + darkfile[i] + fext)
    darkhead = fits.getheader(datadir + darkfile[i] + fext)

print(f"Object observation date: {objhead["DATE-OBS"]}")
print(f"Dark observation date: {darkhead["DATE-OBS"]}")

#part c) Why not print TIME-OBS?
#Object and Dark images dont have to be taken at the same time. 
#Whats more important is that both were taken in the same session or date.
#which is why we printed the DATE-OBS and not the TIME-OBS


# In[5]:


#Andrew Salcedo
#Homework 6: Median Combination
#10/04/2026


# In[6]:


from medcomb import*


# In[31]:


#Problem 2
#b) call median combination function on dark array data, print sepcifc value
comb_dark_arr = medcomb(dark_arr)
print(f"Median value of pixel index (218, 184): {comb_dark_arr[217, 184]}\n")

#c) add HISTORY entry to dark header, saying its the median combined dark frame
#darkhead.append("HISTORYS")
darkhead['HISTORY'] = 'Median Combined dark frame'
#print(darkhead)

#d) write data to new fits file
#fits.writeto('dark_13s_med.fits', comb_dark_arr, darkhead)

#e) subtract median combine dark array from each object frame, write new fits file
sub_obj_arr = obj_arr - comb_dark_arr
#fits.writeto('hw7_asalcedo_prob2_graph1.fits', sub_obj_arr[0], objhead)
print(
f"Indexed pixel of original object frame: {obj_arr[0, 217, 184]}\n"
f"Indexed pixel of subrtracted object frame: {sub_obj_arr[0, 217, 184]}"
)


# In[ ]:




