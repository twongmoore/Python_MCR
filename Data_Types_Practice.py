#!/usr/bin/env python
# coding: utf-8

# # Data Types & Variable Assignment
# This is my first Jupyter Notebook exploring different data types and how you assign variables in python.

# In[1]:


my_name = 'Tom'
print(type(my_name))


# In[2]:


my_favourite_number_text = 'My favourite number is:'
my_favourite_number = 19
print(my_favourite_number_text, my_favourite_number)


# In[3]:


my_favourite_number = 19
my_favourite_number_text = "is my favourite number."
print(my_favourite_number, my_favourite_number_text)


# ## Lists

# In[4]:


my_numbers = [10, 20, 30, 40]
my_numbers[1]


# In[5]:


my_names = ['Andrew', 'Suzanne', 'Eliza', 'Seb']


# In[6]:


my_names[0] = 'Steph'
print(my_names)


# In[7]:


my_names[2:]


# In[8]:


my_names[:2]


# In[9]:


my_names[1:3]


# ## Tuples
# Tuples are like lists, except they are immutable - in other words, their contents cannot be changed later. 

# In[10]:


my_tuple = (10, 20, 30, 40)
my_tuple[3]


# In[11]:


my_tuple[:3]


# In[12]:


my_sliced_tuple = my_tuple[:3]


# In[13]:


my_sliced_tuple == my_tuple[:3]


# ## Arrays
# An array is a data structure consisting of a collection of elements, each identified by at least one array index (or key).

# In[19]:


import numpy as np


# In[20]:


np.random.seed(1234)
my_array = np.random.randint(low=0, high=10, size=(3, 4))


# In[21]:


my_array


# In[22]:


my_array.shape


# ## User-Defined Functions
# If you find yourself writing the same chunk of code again and again, you might want to turn it into a function.

# In[23]:


def bmi(weight, height):
    bmi_value = weight/(height*height)
    return bmi_value


# In[24]:


bmi(87, 1.8)


# In[25]:


def cohen_d(mean1, mean2, sd):  
    effect_size = (mean1 - mean2) / sd  
    return effect_size  


# In[26]:


cohen_d(1020, 1000, 50)


# ## Control Flow Statements
# 

# In[27]:


for i in range(0, 5):
    print('Hi!')


# In[28]:


my_names = ['Tom', 'Suzanne', 'Eliza', 'Seb']


# In[29]:


for element in my_names:
    print(element)


# ## Iterating Over An Array

# In[33]:


weights = np.array([70, 60, 90])
heights = np.array([1.67, 1.77, 1.78])
names = np.array(['Tom', 'Liam', 'Noel'])


# In[34]:


vital_stats = np.array((weights, heights, names))


# In[35]:


print(vital_stats)


# In[36]:


for index in vital_stats:
    print(index)


# In[37]:


vital_stats.T


# In[38]:


for index in vital_stats.T:
    print(index)


# In[39]:


for person in vital_stats.T:
    weight = float(person[0])
    height = float(person[1])
    print(person[2], 'has a BMI of', round(bmi(weight, height)))


# ## Operators
# 

# In[40]:


a = 5
b = 6


# In[41]:


a == b


# In[42]:


a != b


# In[43]:


a = np.array([1, 2, 3])
b = np.array([3, 2, 1])


# In[44]:


a == b


# In[45]:


a + b


# ## Control Flow Statements - While Loops
# Code inside a while loop runs as long as the while loop evaluates to True.

# In[46]:


my_names = ['Tom', 'Liam', 'Noel', 'Bonehead']


# In[47]:


i = 0

while i != 2:
    print(my_names[i])
    i += 1


# ## Control Flow Statements - Conditional
# If statements (and the related elif and else) are conditional statements such that if they evaluate as True the associated code chunk is run, else some other code chunk is run.

# In[48]:


my_first_number = 5
my_second_number = 6


# In[49]:


if my_first_number < my_second_number:
    print(my_first_number, 'is less than', my_second_number)
elif my_first_number > my_second_number:
    print(my_first_number, 'is greater than', my_second_number)
else:
    print(my_first_number, 'is equal to', my_second_number)

