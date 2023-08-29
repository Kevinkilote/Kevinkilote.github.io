#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:46:24 2022

@author: kevin
"""

def rectangle_area(width, height):
        """Calculates the area of a rectangle
        given its width and height as arguments"""
        area = width * height
        return area

my_area = rectangle_area(8,5)
print(my_area)

def greeting(name):
        """Says hi to the person passed in as an argument (must be a string)"""
        print("Hi " + name + "!")

greeting("MOM")

def rectangle_area(width, height):
        """Calculates the area of a rectangle
        given its width and height as arguments"""
        area = width * height
        return area
        
def assinging_func(rect_width, rect_height, app_dict):
    """Assigns a new key-value pair to a dictionary.
    where the key is a tuple of the rectangle's width
    and height, and the value is the area of the rectangle."""
    app_dict[(rect_width, rect_height)] = rectangle_area(rect_width, rect_height)

rect_areas = {}

assinging_func(6, 8, rect_areas)
print("Rectangle area dictionary", rect_areas)
assinging_func(12, 2, rect_areas)
print("Rectangle area dictionary", rect_areas)


names_scores= {"Bob":40, "Monica":80, "Paul":91}
passed_list= []
failed_list= []

def passornot(score_dict, passed_list, failed_list):
    """Function that evaluates if a student is passed or failed,
    and stores the anem of the students accordingly in seperate
    lists. As an argument, it takes a dictionary where the keys
    are the student names and the values are the scores. The two other 
    arguments are two lists to add the names to."""
    for name, score in score_dict.items():
        if score<60:
            failed_list.append(name)
        else:
            passed_list.append(name)
            
passornot(names_scores, passed_list, failed_list)
print("Students passed:", passed_list)
print("Students failed:", failed_list)


def circle_area(r):
    pi= 3.14
    return pi*(r*r)

print(circle_area(3))


def greeting(name, message="Hello, ", times=3):
    print((message + name +"!\n")*times)

print("Only providing the name argument, using the default for the others:")
greeting("Bob")
print("Overwriting the default value for message(order is important) :")
greeting("Bob", "Hi, ")
print("Overwriting the default value for message and times (order is important) :")
greeting("Bob", "Sup, ", 2)


my_area= rectangle_area(8,5)

def rectangle_area(width, height):
    area= width * height
    return area







