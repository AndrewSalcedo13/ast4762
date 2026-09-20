#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
import matplotlib.pyplot as plt


# In[49]:


#Problem 1: Write a code that creates a subsample containing N random draws
#from a Gaussian distribution with a certain width and mean
def Gauss_rand(mu, sigma, N):
    samples = np.random.normal(mu, sigma, N)
    return samples
samples_i = Gauss_rand(55, 13, 10)
print(samples_i)


# In[50]:


#Problem 2: create a sample with N=10 random draws
outputs = []
mu = 55
sigma = 13
N = 10
for i in range(10):
    samples_i = Gauss_rand(mu=55, sigma=13, N=10)
    xbar = np.mean(samples_i)
    sigma = np.std(samples_i)
    outputs_i = [i, xbar, sigma]
    outputs.append(outputs_i)
outputs


# In[51]:


#Problem 4: Write array into text file
with open("practicum2_asalcedo_problem4.txt","w") as txt_file:
    txt_file.write(f"array contains 10 draws\n")
    for row in outputs:
        array = ','.join(map(str, row))
        txt_file.write(f"{array}\n")


# In[52]:


#Problem 5: repeat question 2, 4 for N = 100 . 1,000 . 10,000 . 100,000 . 1,000,000 draws
draws = [10, 100, 1000, 10000, 100000, 1000000]
for N in draws: 
    outputs = []
    for i in range(10):                            #Will loop through only 10 times, creating 10 samples
        samples_i = Gauss_rand(55, 13, N)          #Using N random draws, according to draws
        xbar = np.mean(samples_i)
        sigma = np.std(samples_i)
        outputs_i = [i, xbar, sigma]
        outputs.append(outputs_i)
    with open("practicum2_asalcedo_problem4.txt","a") as txt_file:
        txt_file.write(f"array contains {N} draws\n")
        for row in outputs:
            array = ','.join(map(str, row))
            txt_file.write(f"{array}\n")


# In[53]:


#Problem 6: find standard deviation of means of sample sizes
#Reading data means in from txt file
smeans = {} #make empty dictionary
with open("practicum2_asalcedo_problem4.txt", "r") as txt_file:
    lines = txt_file.readlines()
for line in lines:
    if line.startswith("array"):    #If line starts with 'array' creates empty array for that N value
        parts = line.split()
        N = int(parts[2])
        smeans[N] = []
    elif line.startswith("sample size"):
        continue
    else:                           #otherwise stores median from the given sample line according to its N
        parts = line.split(",")
        mean = float(parts[1])
        smeans[N].append(mean)

#Calculating the standard deviation of the means
with open("practicum2_asalcedo_problem4.txt","a") as txt_file:
    txt_file.write("sample size,   Standard deviation of mean\n")
    std_smeans = []
    for N in smeans:
        std = np.std(smeans[N])
        std_smeans.append(std)
        print(N, std)
        txt_file.write(f"{N}, {std}\n")


# In[54]:


#Problem 7
plt.figure()
plt.loglog(draws, std_smeans)
plt.xlabel("Sample size")
plt.ylabel("Std. Dev. of mean")
plt.title("log plot of std. dev. of mean vs sample size")
plt.savefig("practicum2_asalcedo_problem7_graph1.png")
plt.show()


# In[ ]:




