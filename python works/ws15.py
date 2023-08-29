#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:49:44 2022

@author: kevin
"""

class Cat:
    """Docstring"""
    
    animal_type= "carnivore"
    
    def __init__(self, name, color, hair, age):
        self.name= name
        self.color= color
        self.hair= hair
        self.age= age
        self.property= "cute"
    
    def describe(self):
        """Docstring"""
        return "{} is {} years old".format(self.name, self.age)
        
    def say(self, sound):
        return "{} says {}".format(self.name, sound)

class Munchkin(Cat):
    
    characteristics= "very short legs"
    
    def __init__(self, name, color, age, weight, hair="short"):
        super().__init__(name, color, hair, age)
        self.weight= weight
        
    
    def say(self, sound="nyan"):
        return "{} says {}".format(self.name, sound)
    
    def cat_info(self):
        info_dict= {"name":self.name, "color":self.color, "age":self.age, "hair":self.hair}
        return info_dict
    
    def another_describe(self):
        return super().describe() + " and " + self.color
    
    
class Persian(Cat):
    def say(self, sound="meow"):
        return "{} says {}".format(self.name, sound)


class Siamese(Cat):
    def say(self, sound="nyan"):
        return "{} says {}".format(self.name, sound)



luna= Persian("Luna", "white", "long", 2)
milo= Siamese("Milo", "gray", "short", 4)
oliver= Munchkin("Oliver", "black", 1, 2.4)
print(oliver.name+"'s hair is", oliver.hair)
loki= Munchkin("Loki", "black", 7, 4.2, "long")
print(loki.name+"'s hair is", loki.hair)
print(loki.describe())
print(loki.another_describe())
print(loki.name,"is", loki.animal_type, "but has", loki.characteristics)
print(loki.name, "is", loki.property)
loki.property= "very cute"







        