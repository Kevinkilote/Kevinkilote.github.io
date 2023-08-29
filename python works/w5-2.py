#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:55:51 2022

@author: kevin
"""

scientist_dictionary={'Da Vinci':1452,'Galilei':1564,'Newton':1642}
print(len(scientist_dictionary))
random_dictionary={23:'abcd', 14.678:34,'abc':[1,2,3]}
print(scientist_dictionary['Galilei'])
print(scientist_dictionary)
scientist_dictionary['Da Vinci']= 1519
print(scientist_dictionary)
scientist_dictionary['Darwin']= 1809
print(scientist_dictionary)

for name in scientist_dictionary:
    print(name)
for name in scientist_dictionary.keys():
    print(name)
for date in scientist_dictionary.values():
    print(date)

for name,date in scientist_dictionary.items():
    print('The name of the scientist',name,', Corresponding date:', date)
    
gpu_dict={
"nvidia":{
"GPU model": "3090 Ti",
"MSRP": False,
"launch year": 2022,
"manufacturers":['Gigabyte', 'MSI', 'Zotac']},
"amd":{
"GPU model": "RX 6800 XT",
"MSRP":False,
"launch year": 2020,
"manufacturers":['MSI','Asrock']}
    }
