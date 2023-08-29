#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Christopher Kevin Siswanto
Student ID: 26002204494
Program description: adding up each variables and break the loop once it reaches
more than the sum intended using zip and break.

"""

number_list_1=[1,2,3,4,5,6,7,8,9,10,11]
number_list_2=[10,11,12,13,14,15,16,17,18,19,20]

print("Length of the first list:",len(number_list_1))
print("Length of the second list:",len(number_list_2))
for number_1,number_2 in zip(number_list_1,number_list_2):
    summa= (number_1+number_2)
    print("The sum is {}".format(summa))
    if summa>25:
        break
    
