#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Andrew Salcedo
#Homework 2
#September 7, 2026


# In[38]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# In[46]:


#PROBLEM 2
print("Probelm 2: Without using loops write the necessary Python commands that:\na)")
print(" a1) Creates an array of integers x from 0 to 1000 (up to and including 1000). How many elements do you need?")
x = np.arange(0.0, 1001.0)
print(f"x={x}\nThe array must have 1001 elements, going from 0 to 1001 in order to include 1000")
print(" a2) Prints the datatype of the array and the array’s minimum and maximum.")
print(f"type:{type(x)}, minimum:{x.min()}, maximum:{x.max()}\n")

print("b\n b1) Re-scale x to contain values from 0 to 2π. Don’t make a new array, re-scale the array of question 2a.")
x *= (2*np.pi)/1000
print(x)
print(f" b2) Print the minimum and maximum values of the new x array\nminimum:{x.min()}, maximum:{x.max()}\n")

print("c) Make an array y whose values are the sine of the values of x")
y = np.sin(x)
print(f"{y}\n")

print("d) Print the value of element 234 of y [Note the difference between the 234th element and element 234 in Python]")
print(f"{y[234]}")
print(
    "lists and arrays begin at index 0 while elements start at 1,"
    "so the 234th element would be at index 233 while element 234 would be at"
    "index 234, they dont have the same position" 
)


# In[64]:


#PROBLEM 3
get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('matplotlib', 'widget')
print("Problem 3: Write the necessary Python commands that:")
print("a) Plot y vs. x from problem 2c. Make the plot publication-ready using reasonable axis labels etc")
plt.figure()
plt.plot(x, y)
plt.title("y=sin(x)")
plt.xlabel("x(radians)")
plt.ylabel("sin(x)")
plt.show()

print("b) Save your plot as a PNG using the appropriate Python commands (no screenshots or window dumps from outside Python).")
plt.savefig("hw2_asalcedo_problem3_graph1")


# In[71]:


#PROBLEM 4
get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('matplotlib', 'widget')
print("Problem 4 \na) \n a1)Make a “ramp” array r with 101 evenly spaced elements going from -1 to +1")
r = np.linspace(-1.0, 1.0, 101)
print(r)
print(
" a2)'Clip', or mask, the array so that any value greater than 0.5 is set to 0.5 and"
" any value less than -0.5 is set to -0.5. There are  different ways that you can do"
" this with numpy, but remember, no loops!"
       )
r_clip = np.clip(r, -0.5, 0.5)
print(r_clip)

print("b)\n b1) In the same plot, plot the original and clipped arrays. Your figure should look something like this ")
plt.figure()
plt.plot(r)
plt.plot(r_clip)
plt.title("ramp vs. clipped ramp")
plt.xlabel("x: index")
plt.ylabel("y: value")
plt.legend(['ramp', 'clipped ramp'])
plt.show()
plt.savefig("hw2_asalcedo_problem4_graph1.pdf")


# In[98]:


#PROBLEM 5
print(
"problem 5\nGive the URLs of two web sites outside of UCF that provide free"
" astronomical software that is written in Python. Write a paragraph about each package"
" in your own words. Put the two paragraphs as an extended string (between sets of triple"
"single-quotes) in your main homework file."
)
print(
    "URL 1: https://docs.astropy.org/en/stable/ \n"
    "Above is a URL to the astropy website, astropy is community python library for astronomers. It is filled with general tools "
    "such as fu-nctions, classes and other commands commonly used in the astronomy and astrophysics. Astropy isn't exclusive to the "
    "field of physics or astronomy either as it was founded to create a basic framework to help reduce the common and redundant tasks "
    "and instead help focus on creating more complex tools and code with ease. Astropy is a growing community of collaborators "
    "ultimately dedicated to eventaully cre-ating a common core package for the field of astronomy and astrophysics in python.\n"
)
print(
    "URL 2:https://spiceypy.readthedocs.io/en/stable/\n"
    "Above is a website explaining the SpicyPy package and library. SpicyPy is a python wrapper for the SPICE toolkit, developed by"
    " and for NASA, making it compatible across multiple systems and languages such as python. SPICE(space, planet, instrument, "
    "c-matrix, events) ob-servation geometry system for space science mission provides access and tools to help in planning and "
    "interpreting scientific observat-ions as well as supporting engineering tasks on missions. However now its use has been  expanded "
    "to cover a large variety of fields and research within astronomy. "
)




# In[ ]:




