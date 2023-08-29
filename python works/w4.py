#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:58:55 2022

@author: kevin
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