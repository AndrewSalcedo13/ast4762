#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Salcedo
#Homework 3, Plot functions
# 9/13/26


# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import hw3_asalcedo_support_functions as hw3_supp_funcs


# In[2]:


test_square_1 = np.arange(0,9)
print(f"test square 1:\n{test_square_1}")
print("result 1:\n", hw3_supp_funcs.square(test_square_1))

test_square_2 = np.arange(0.0,25.0).reshape(5,5)
print(f"\ntest square 2:\n{test_square_2}")
print("\nresult 2:\n", hw3_supp_funcs.square(test_square_2))


# In[3]:


hw3_supp_funcs.squareplot(1, 7, 5, 'hw3_asalcedo_problem3_graph1')


# In[ ]:




