#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Christopher Kevin Siswanto
Student ID: 26002204494
Program description: adding up all even numbers until 300 using calculations and
conditional statements nesting.
    
"""

number=1
total=0

while number<=300:   
    if(number%2)==0:
        total+=number
        number+=2
    else:
       number+=1

print(total)