#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
Author: Christopher Kevin Siswanto
Student ID: 2600220449-4
Program description: This program is written to read a given file
and changes it to a numpy array. Afterwards, creates a 1-D array of 30 values. 
Then the program adds the 1st array and the array from the given file. 
Thirdly, it creates a 1-D number random array with 30 floating point numbers.
The program then joins both arrays. Lastly, it gets the average of the first
1-D array and the sum of the second 1-D array.
"""

import numpy as np
from numpy import random

def make_array(filename):
    """ Reads the given file, and then converts contents/values into floating
    point numbers by using an empty list and populate it utilizing a for loop.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text_array = f.read().splitlines()
        lst = []
        for i in text_array:
            floats = float(i)
            lst.append(floats)
        return np.array(lst)

read_arr = make_array("numbers.txt")
print("Array created from the numbers of the text file:\n", read_arr)
print("Type of read_arr:", type(read_arr))


arr_1 = np.linspace(5, 100, num = 30)

arr_1 = arr_1 + read_arr

arr_2 = random.rand(30)

stacked_array = np.stack((arr_1, arr_2), axis=0)
print("Stacked array:\n", stacked_array)

average = np.mean(stacked_array[0])
print("Average of the stacked array[0]:", average)

summa = np.sum(stacked_array[1][0:5])
print("Sum of the first 5 elements of stacked_array[1]:", summa)