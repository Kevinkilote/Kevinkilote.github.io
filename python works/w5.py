#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:44:18 2022

@author: kevin
"""

our_list= ['Pythagoras',427,'Plato',['apple','a plum', 3], True,'Aristotle']
print('Our list:', our_list)
print('The first element in the container is', our_list[0])
print('Type of the second element is', type(our_list[1]))
print('Length of our list is', len(our_list))
print("Length of Pythagoras' is", len(our_list[0]))

print('List inside our list:', our_list[3])
print(type(our_list[3]))
print('Length of the list inside our list is', len(our_list[3]))
print('The first element in the list inside our list is', our_list[3][0])
print('The second element in the list inside our list is', our_list[3][1])
print(type(our_list[[3][0]]))


for element in our_list:
    print(type(element))

print('The last element in our list is', our_list[-1])
print('The second to last element in our list is', our_list[-2])

print('The first two elements from our_list are', our_list[0:2])
print('With notation index 3 to 5:', our_list[3:5])
our_new_list= our_list[1:4]
print(our_new_list)
print(our_new_list[1:2])
print(our_new_list[:2])
print(our_new_list[1:])

my_list2= [1, True, 'three', 4.5]
print(my_list2)
my_list2[2]= 'four'
print(my_list2)
my_list2[1]='4'
print(my_list2)

another_list= ['B','This is a sentence.','459',['B','C',127.45]]
for element in another_list:
    if 'This' in element:
        print(element)
    if 'B' in element:
        print(element)

for index, element in enumerate(another_list):
    if 'a' not in element:
        print('Index', index, 'Element', element)
        


    
    
    
    



