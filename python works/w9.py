#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:26:14 2022

@author: kevin
"""

def f():
    n = 5
    return n*2
print("Calling function f and printing the returned value:", f())


def function_f():
    n = 5
    print(n)
def function_g():
    n = "Just a string"
    print(n)

print("Calling the function function_f:")
function_f()
print("Calling the function function_g:")
function_g()

x = 7

def function_f(y):
    return(x*y)

print("Calling function function_f and printing the returned value:", function_f(3))

file = open("w9.txt", 'w', encoding="utf-8")
file = open("/Users/kevin/Documents/w9.txt", 'w', encoding="utf-8")
file = open("w9.txt", 'r+', encoding="utf-8")
file.close()

with open("w9.txt", 'w', encoding='utf-8') as f:
    f.write("File starts\n")
    f.write("This is a line\n")
    f.write("Another line..")
    f.write("Another string")
    
with open("w9.txt", 'r', encoding='utf-8') as f:
    data = f.read()

print(data)

with open("w9.txt", 'r', encoding='utf-8') as f:
    data = f.readlines()
    
print(data)
print(type(data))

with open("w9.txt", 'r', encoding= 'utf-8') as f:
    data = f.read().splitlines()
    
print(data)


my_numbers= [1,2,4,6,76,8,9,9]

with open("testw9.txt", 'w', encoding= 'utf-8') as f:
    for number in my_numbers:
        f.write(str(number)+"\n")

with open("testw9.txt", 'r', encoding= 'utf-8') as f:
    data = f.read().splitlines()
    
print(data)
print("Type of the list elements:", type(data[0]))

new_data=[]
for i in data:
    new_data.append(int(i))

print(new_data)
print("Type of the new list elements:", type(new_data[0]))

