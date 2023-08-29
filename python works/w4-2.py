#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:48:46 2022

@author: kevin
"""

points=23
if points>=90:
    print('A+')
elif points>=80:
    print('A')
elif points>=70:
    print('B')
elif points>=60:
    print('C')
else:
    print('F')

if points>=0:
    if points==0:
        print('zero')
    else:
        print('positive')
else:
    print('negative')
    