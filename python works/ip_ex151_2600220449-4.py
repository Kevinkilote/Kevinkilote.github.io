#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Christopher Kevin Siswanto
Student ID: 2600220449-4
Program description: This program is designed to make a simulation.
In this program, there is the 'Adventurer' class, and the 'Healer' class. The 'Adventurer' 
class has the 'intro' function for introducing the names and the 'need heals' 
function to decide if the adventurer needs to be healed based on
an if method. The 'Healer' class has the 'healer_intro' function and the 'heal' function
that serves to heal the adventurers, the it prints back the healed health information of
the adventurers. 

"""

from numpy import random


class Adventurer:
    """
    Instantiation of the Adventurer class defines an object with class
    attribute maximum health, and instance attributes name and (current) health.
    An Adventurer can introduce itself, and has an instance method that decides 
    if the Adventurer needs healing or not.
    """
    max_health = 100

    def __init__(self, name):
        self.name = name
        self.health = random.randint(60, 91)

    def intro(self):
        """
        Adventurer introduction.
        Returns a string.
        """
        print("Hello my name is " + self.name +"!")
        
    def needs_heal(self):
        """
        Checks the adventurer if the health is under 80, and prints
        "I need healing" If the user does not, no heal and prints "I'm fine!""
        """
        if self.health < 80:
            print("I need healing!")
            return True
        else:
            print("I'm fine!")
            return False


class Healer(Adventurer):
    """
    The healer class inherits from the adventurer classthe healer has an
    instance method to  heal the adventurer.
    """

    def __init__(self, name, medicine_stock):
        super().__init__(name)
        self.medicine_stock = medicine_stock

    def healer_intro(self):
        """
        Gives an introduction of the healer and utilizes the adventurer 
        introduction method prints the current medicine stock
        """
        self.intro()
        print("My current medicine stock is {}.".format(self.medicine_stock))

    def heal(self, adventurer):
        """
        Heals the Adventurer if medicine stock is available, if not, no heals 
        and prints out of medicine
        """
        heal_value = adventurer.max_health - adventurer.health

        if self.medicine_stock == 0:
            print("I'm out of medicine, sorry!")
            return


        if heal_value > self.medicine_stock:
            print("I can only help this much, sorry!")
            adventurer.health += self.medicine_stock
            self.medicine_stock = 0
            return

        print("Here you go, fully healed!")
        adventurer.health = adventurer.max_health
        self.medicine_stock -= heal_value

        return


healer = Healer("Bob the Healer", 80)
adventurers = ["Ray", "Tom", "Kenny", "Ajax", "Kiara"]
healed_list = []

for name in adventurers:
    print()

    adventurer = Adventurer(name)
    adventurer.intro()

    if adventurer.needs_heal():
        print("Health of", adventurer.name, "is", "{}".format(adventurer.health))
        healer.healer_intro()
        healer.heal(adventurer)
        print("Health of " + adventurer.name + " now is " + "{}".format(adventurer.health))

    healed_list.append((adventurer.name, adventurer.health))

print("\n", healed_list)