#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:49:11 2022

@author: kevin
"""

languages_1= {"FORTRAN":1957, "LISP":1958, "COBOL":1959}
languages_2= {"SNOBOL": 1962, "BASIC": 1964}
print("Original dictionary:", languages_1)
languages_1.pop("LISP")
print("Modified dictionary:", languages_1)
popped_elem= languages_1.pop("COBOL")
print("2x modified dictionary:", languages_1)
print("The popped element:", popped_elem)





our_list= []
i=0
while len(our_list)<10:
    our_list.append(i)
    i+=1

print("Our list:", our_list)
print("The length of our list:", len(our_list))
maximum= max(our_list)
minimum= min(our_list)

print("maximum:", maximum, "\nminimum:", minimum)
