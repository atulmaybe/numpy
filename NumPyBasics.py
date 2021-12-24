#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# to chekc numpy version
print(np.__version__)


# In[3]:


# NumPy is used to work with arrays. Arrays in numpy is called as ndarray
# We can create a NumPy ndarray object by using the array() function.
array = np.array([1,2,3,4,5])


# In[4]:


print(array)


# In[6]:


print(type(array))


# In[7]:


# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
# and it will be converted into an ndarray


# In[8]:


arr = np.array((1,2,3,4))


# In[10]:


print(arr)


# In[11]:


# dimensions in array 
oneD = np.array(12)
print(oneD)


# In[13]:


# two dimensional array

twoD = np.array([[1,2,3],[4,5,6]])
print(twoD)


# In[20]:


# three dimensional array 
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
threeD = np.array([[[1,2,3,4],[3,4,5,6]],[[6,7,8,9],[2,3,6,7]]])
print(threeD)


# In[24]:


# Check Number of Dimensions
# ndim object returns dimension of the array
print(threeD.ndim)
print(twoD.ndim)
print(oneD.ndim)


# In[25]:


# you can create array with n dimension 
arr = np.array([1,4,7,89],ndmin=7)
print(arr.ndim)


# In[26]:


# accessing elements of One dimensional array by index 
arr = np.array([1,2,3,4,5])
print(arr[0])


# In[27]:


print(arr[2]+ arr[4])


# In[28]:


for i in arr:
    print(i)


# In[42]:


# accessing elements of Two dimensional array by index 
arr = np.array([[1,2,3,4,5],[11,22,33,44,55]])
print(arr[1,2])


# In[41]:


print(arr[1,2])


# In[45]:


# array slicing 
arr = np.array([1,2,3,4,5])
slicedArr = arr[0:3]
print(slicedArr)


# In[46]:


print(arr[3:])


# In[47]:


print(arr[:3])


# In[48]:


# Note : The result includes the start index, but excludes the end index.


# In[49]:


# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''


# In[53]:


# Checking the Data Type of an Array
arr = np.array([1,2,3,4])
print(arr.dtype)


# In[55]:


arr = np.array(['atul','bhushan','chandan'])
print(arr.dtype)


# In[56]:


# Creating Arrays With a Defined Data Type
arr = np.array([1,2,3,4], dtype="S")
print(arr.dtype)


# In[57]:


# Converting Data Type on Existing Arrays
newArr = arr.astype('i')
print(newArr.dtype)


# In[59]:


print('hi')


# In[ ]:




