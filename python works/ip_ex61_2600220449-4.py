#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Christopher Kevin Siswanto
Student ID: 2600220449-4
Program description: Using techniques such as integrating dictionaries and 
adding more components into the list using update, adding, and also removing 
objects and values with different methods.

"""

scientist_list_1= ['Einstein', 'Curie', 'Newton', 'Darwin']
scientist_list_2= ['Tesla', 'Galilei', 'Lovelace']
scientist_list= scientist_list_1 + scientist_list_2

scientist_list_3= ["Hawking", "Faraday"]
for scientist in scientist_list_3:
    scientist_list.append(scientist) # append to update/add elements to list

    
print("Length of the scientist list:", len(scientist_list))

scientist_list.reverse() # printing the elements but backwards
print("Reversed scientist list:", scientist_list)

scientist_dict= {}

for index, scientist in enumerate(scientist_list):
    scientist_dict[scientist]= index
    
scientist_dict_2= {"Faraday":1, "Boyle":9}
scientist_dict.update(scientist_dict_2) # updates the elements of the dictionary
print("The scientist dictionary:", scientist_dict)

index_list= list(scientist_dict.values())
numbers= index_list[0:5]
print("Numbers list:", numbers)

one=numbers.pop(0) #removes the element and can be used for further uses later

for number in numbers:
    if (number % 2) !=0:
        numbers.remove(number)

print("The number list filtered out of odd numbers:", numbers)
maximum= max(numbers)
print("The maximum value in the number list:", maximum)
