#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:47:02 2022

@author: kevin
"""

my_tuple= (10, 20, 30, 40)
number_1, number_2, number_3, number_4= my_tuple
print("For example number 2:", number_2)

scientist_dictionary= {'Da Vinci':1452, 'Galilei':1564, 'Newton':1642}
elements= list(scientist_dictionary.items())
print("List of dictionary items in a list of tuples:", elements)
print("First element:", elements[0])


language_set1={"FORTRAN", "COBOL", "LISP"}
language_set2={"C++", "COBOL"}
print("original language sets:", language_set1, ",", language_set2)
inter= language_set1.intersection(language_set2)
diff= language_set1.difference(language_set2)
print("Elements that exist in both language set 1 and language set 2", inter)
print("Elements that only exist in language set 1 and not in language set 2", diff)
language_set1.update(language_set2)
print("Updated language set 1:", language_set1)


my_list= ["FORTRAN", "COBOL", "FORTRAN", 1,2,2]
my_set= set(my_list)
print("Original list:", my_list, '\ntype:', type(my_list))
print("Duplicates removed:", my_set, '\ntype:', type(my_set))
my_list= list(set(my_list))
print("The list with duplicates removed:", my_list, '\ntype:', type(my_list))

my_list= ["FORTRAN", "COBOL", "FORTRAN", 1,2,2]
my_list= list(dict.fromkeys(my_list))
print("Duplicates removed and order preserved:", my_list)

my_tuple= ("apple", "apple", "orange")
my_set= {"apple", "apple", "orange"}
print("My tuple:", my_tuple, '\nMy set:', my_set)
print('The word (string) "orange" is not an element the tuple:', "orange" in my_tuple)
print('The word (string) "lemon" is not an element of the set:', "lemon" not in my_set)

my_string= "the phenomenon time dilation is the difference in the elapsed time as measured by two clocks"
split_string= my_string.split()
print("The split string in a list:", split_string)

