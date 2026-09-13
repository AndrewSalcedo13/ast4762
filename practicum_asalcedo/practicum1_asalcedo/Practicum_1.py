#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


# In[65]:


#Problem 1
print(
    "a) Make a 300×200 Float64 array. Each array element should contain its own x coordinate,"
"starting with x = 0 for column 0 and ending with x = 299 for column 299 (i.e., column 0 has 200 zeros)."
"Do this using a loop\n"
)
array = np.zeros((300,200))      #creates an array(or matrice) with this number of rows, columns
for i in range(array.shape[0]):  #.shape[1] tells it to grap the number of columns and loop through that many times
    array[i, :] = i              #grabbing all the rows within column i and setting the columns will equal their indice
print(array.dtype)
print(array)

print(
    "b) same problem but now do it without using a loop\n"
)
#the work below is what the professor showed in class for how to answer the problem without using a loop
coo = np.arange(300)
coo.shape = (300,1)
arr = np.zeros((300,200))
print(arr.dtype)
arr+=coo
print(arr)
plt.imshow(arr, cmap = 'gray', origin = 'lower')  #(c

#d)
i = 5    #desired row to check
print(f"\nrow: {i}\narray:{array[i, :]}")


# In[17]:


#Problem 2
hdul = fits.open("m42_40min_ir.zip")   #Opens file
hdul.info()                            #reads and tells information within file
image = hdul[0].data                   #Image stored in HDU this accesses that data
print(image.shape)                     #checks shape of (image)array inside
print(type(image))                     #checks what data type image is

plt.imshow(image, cmap = 'gray', origin = 'lower')
plt.title('m42_asalcedo')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('practicum1_asalcedo_problem3_graph1.png')
plt.show()


# In[ ]:




