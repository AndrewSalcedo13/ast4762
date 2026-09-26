#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Andrew Salcedo
#Homework 4, fits and probabilities
#9/20/26


# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[20]:


#Problem 2: Gaussian Distribution in python
#2a) Python function that draws random sample of N values from a gaussian dist.
N = 10000      #number of values drawn from gaussian distribution
mu = 55         #mean of gaussian distribution
sigma = 13      #standard deviation of gaussian distribution
Gauss_rand = np.random.normal(mu, sigma, N)

#2b) create histogram from previous distribution samples
plt.hist(Gauss_rand, bins = np.arange(0,101, 1))
plt.title("Histogram of Gaussian")
plt.xlabel("Values drawn, x")
plt.ylabel("How many times drawn, N(x)")
plt.savefig("hw4_asalcedo_problem2b_graph1.png")

#2c) Use gaussian function to overplot a gaussian distribution
bin_centers = np.arange(0.5, 100, 1)     
#approximated center of each bin to avoid integration
Gaussian_func = (sigma * ( (2*np.pi))**0.5 )**-1 * np.exp(-((bin_centers-mu)**2)/(2 * sigma**2)) 
#Gaussian function to approximate each value
bin_Gdist = N * Gaussian_func                
#Multiply by N draws to find the gaussian function for each bin, not just value

plt.plot(bin_centers, bin_Gdist, color = 'r')
plt.savefig("hw4_asalcedo_problem2c_graph1.png")
plt.show()

