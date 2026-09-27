#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy
import matplotlib.pyplot as plt
from linfit import *


# In[109]:


#linfit?


# In[110]:


#Problem 1
print("part a)")
data = np.loadtxt("practicum3_1.dat")
#data 1, made using f(x) = 3.2x + 1.2
d1x = data[0:100, 0]
d1y = data[0:100, 1]
#data 2, made using f(x) = 3.2x^2 + 1.2, for added noise
d2x = data[100:, 0]
d2y = data[100:, 1]
#plotting data 1
plt.figure()
plt.plot(d1x, d1y, '.')
plt.title("Data 1 plot")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show

print("part b)")
#fit data 1 to linear model
linfit1 = linfit(d1y, d1x, 0.5)
#fitted parameters
a1f = linfit1[0]      #fitted intercept
b1f = linfit1[1]      #fitted slope
a1f_unc = linfit1[2]  #std of fitted intercept
b1f_unc = linfit1[3]  #std of fitted intercept
#within 3 std
a1 = 1.2              #intercept of model 1
b1 = 3.2              #slope of model 1
a1_std = (np.abs(a1f - a1))/(a1f_unc)
print(f"a1_std={a1_std}")
b1_std = (np.abs(b1f - b1))/(b1f_unc)
print(f"b1_std={b1_std}")
print("the fitted parameters of model 1 are within 3 std of the parameters of the true line")

print("part c)")
prob1 = linfit1[5]
chis1 = linfit1[4]
yfit1 = linfit1[7]
print(f"chis1 = {chis1}")
print(f"prob = {prob1}")
print(f"there is a {prob1*100}% chance of getting a higher chi square")
plt.figure()
plt.plot(d1x, d1y, '.', label = 'data 1')
plt.plot(d1x, yfit1, label = 'fitted model', color = 'r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("data 1 vs. linear fitted model 1")
plt.legend()
plt.savefig("practicum3_asalcedo_problem1c_graph1.png")
plt.show()

print("part d)") #repeating parts b and c but for model 2
#fit data 2 to linear model
linfit2 = linfit(d2y, d2x, 0.5)
#fitted parameters
a2f = linfit2[0]      #fitted intercept
b2f = linfit2[1]      #fitted slope
a2f_unc = linfit2[2]  #std of fitted intercept
b2f_unc = linfit2[3]  #std of fitted intercept
#within 3 std
a2 = 1.2              #intercept of model 2
b2 = 3.2              #slope of model 2
a2_std = (np.abs(a2f - a2))/(a2f_unc)
print(f"a2_std = {a2_std}")
b2_std = (np.abs(b2f - b2))/(b2f_unc)
print(f"b2_std={b2_std}")
print("the fitted parameters of model 2 are NOT within 3 std of the parameters of the true line")

prob2 = linfit2[5]
chis2 = linfit2[4]
yfit2 = linfit2[7]
print(f"chis2 = {chis2}")
print(f"prob2 = {prob2}")
print(f"there is a {prob2*100}% chance of getting a higher chi square")
plt.figure()
plt.plot(d2x, d2y, '.', label = 'data 2')
plt.plot(d2x, yfit2, label = 'fitted model', color = 'r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("data 2 vs. linear fitted model 2")
plt.legend()
plt.savefig("practicum3_asalcedo_problem1d_graph1.png")
plt.show()


# In[112]:


#Problem 2
#a)
CCD = np.array([])
CCD = np.append(CCD, np.random.poisson(10000,396))     #396 random poisson distributed values
CCD = np.append(CCD, np.random.uniform(0, 10**6, 4))   #4 random unifrom distributed values
CCD_mean = np.mean(CCD)
CCD_med = np.median(CCD)
print(f"CCD sample-\nmean: {CCD_mean}\nmedian: {CCD_med}")
#N is the number photons detected per 'pixel'(element), so N = 10000. The median is closer to N being off by on ly 8.5,
#as opposed to the mean which is off by 3567.676598214188(this is caused by the 'bad' pixels)

#b)
CCD_std = np.std(CCD)
print(f"std: {CCD_std}\n")

#masked sub-sample
CCD_ss = CCD[ ( CCD_med - (5 * CCD_std) < CCD) & (CCD < CCD_med + (5 * CCD_std)) ]
CCD_ss_mean = np.mean(CCD_ss)
CCD_ss_med = np.median(CCD_ss)
CCD_ss_std = np.std(CCD_ss)
print(f"CCD subsample-\nmean: {CCD_ss_mean}\nmedian: {CCD_ss_med}\nstd: {CCD_ss_std}")

#The new mean median and std represent the sample much more accurately, because the median was used as opposed to the mean,
#which was heavily affected by the 4 'bad' pixels and their much large(and thus more heavily weighted) values.


# In[ ]:




