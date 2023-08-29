#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Christopher Kevin Siswanto
Student ID: 2600220449-4
Program description: The program is intended to take the nested list and
flattens it using a function with its own arguments, after that it filters
the positive numbers and stores them in two different list by odd and even 
numbers. It then removes the duplicate numbers and shows the unique numbers.
    
"""
    
num_lst = [[1,1,4,66], [-55,7], [-1,43,55,-6,12,12,4]]
even_numbers = []
odd_numbers = []

def flatten_list(a_list):
    """Takes the list and flattens it by turning the nested list and changing
    it to a normal list."""
    flat_num_lst = []
    for lst in a_list:
        for element in lst:
            flat_num_lst.append(element)

    return flat_num_lst

def filter_numbers(number_list, evens = even_numbers, odds = odd_numbers):
    """Filters the numbers in a list to be stored as positive numbers
    in odd and even numebers list. It has 3 arguments which is the
    number list, the even numbers and odd numbers."""
    for i in number_list:
        if i >= 0:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

def remove_dups(a_list):
    """Removes duplicates from a list and returns the list with the
    order intacted."""
    dups_removed = list(dict.fromkeys(a_list))
    return dups_removed


print("Original nested list:", num_lst)

flat_num_lst = flatten_list(num_lst)
print("Flattened list:", flat_num_lst)

filter_numbers(flat_num_lst)
print("The even numbers:", even_numbers)
print("The odd numbers:", odd_numbers)

uniq_even_numbers = remove_dups(even_numbers)
uniq_odd_numbers = remove_dups(odd_numbers)
print("The unique even numbers:", uniq_even_numbers)
print("The unique odd numbers:", uniq_odd_numbers)