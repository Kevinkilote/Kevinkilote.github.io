#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:44:51 2022

@author: kevin
"""

import math
print(math.pi)
print(math.e)

from math import pi
print(pi)

from math import *
print(pi)
print(e)
print(factorial(4))

from math import *
print(factorial(4))

def factorial(number):
    return number*2

print(factorial(4))

import math as m
print(m.pi)

from math import e as euler_n
print(euler_n)

import numpy as np
arr_1= np.array([1, 10, 15])
arr_2= np.array([[1.3, 2.5, 3.5], [1.22, 1.2, 2.33]])
print("This is how our first array looks like:", arr_1)
print("The shape of the first array:", arr_1.shape)
print("This is how our second array looks like:", arr_2)
print("The shape of the second array:", arr_2.shape)
print("The number of dimensions of the second array:", arr_2.ndim)
print("Python data type of the arrays:", type(arr_1), type(arr_2))
print("NumPy data type of the second array:", arr_2.dtype.name)
print("How many elements are in the second array?", arr_2.size)

import numpy as np
arr= np.zeros((2,4))
print(arr)
arr= np.ones(5)
print(arr)
arr= np.arange(5)
print(arr)
arr= np.arange(5, 18, 3)
print(arr)
arr= np.linspace(0, 20, num=7)
print(arr)

my_list= [[1.23, 5.44, 5.3], [0.1, 5.0, 1.44]]
print(my_list,"\n")
my_array= np.array(my_list)
print(my_array, type(my_array))

arr= np.arange(2, 11, 2)
print(arr, "\n")
lst= list(arr)
print(lst, type(lst))

arr= np.array([2, 1, 6, 7, 8, 9, 97, 6, 8])
print(np.sort(arr))

arr_1= np.array([1, 2, 3, 4])
arr_2= np.ones(4)
print("First array:", arr_1)
print("Second array:", arr_2)
print("Added together:", arr_1 + arr_2)

arr_1= np.array([[1, 2, 3], [4, 5, 6]])
arr_2= np.array([[2, 3, 4], [5, 6, 7]])
concated= np.concatenate((arr_1, arr_2))
print(concated)

arr_1= np.arange(8)
print(arr_1)
arr_2= arr_1.reshape(2,4)
print(arr_2)

arr= np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("command arr[1]:", arr[1])
print("command arr[1:3]:", arr[1:3])
print("command arr[1][2]:", arr[1][2])

from numpy import random
arr_1= random.randint(50, size= (4,5))
print(arr_1, "\n")

arr_2= random.rand(4)
print(arr_2, "\n")

arr_3= random.rand(4, 2, 3)
print(arr_3)


