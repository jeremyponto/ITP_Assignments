# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:27:48 2019

@author: user
"""

# 1
def convert_to_days():
    hours = float(input('Enter number of hours: '))
    minutes = float(input('Enter number of minutes: '))
    seconds = float(input('Enter number of seconds: '))
    days = get_days(hours, minutes, seconds)
    print('The number of days is:', str(days))  
def get_days(hours, minutes, seconds):
    days = hours / 24 + minutes / 1440 + seconds / 86400
    return round(days, 4)
convert_to_days()

# 2
def calc_weight_on_planet(weight_on_earth, gravity = 23.1):
    mass = weight_on_earth / 9.8
    weight_on_planet = mass * gravity
    print(weight_on_planet)
calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)

# 3
def num_atoms(weight, atomic_weight = 196.97):
    mole = weight / atomic_weight
    number_of_atoms = mole * 6.022 * 10 ** 23
    return number_of_atoms
number_of_atoms = num_atoms(10)
print(number_of_atoms)
number_of_atoms = num_atoms(10, 12.001)
print(number_of_atoms)
number_of_atoms = num_atoms(10, 1.008)
print(number_of_atoms)

# 4
def calc_new_height():
    current_width = float(input('Enter the current width: '))
    current_height = float(input('Enter the current height: '))
    desired_width = float(input('Enter the desired width: '))
    corresponding_height = desired_width / current_width * current_height
    print('The corresponding height is:', str(corresponding_height))
    return corresponding_height
corresponding_height = calc_new_height()
print(corresponding_height)

# 5
def convert_temp():
    Tf = int(input('Enter a temperature in Fahrenheit: '))
    print('The temperature in Fahrenheit is:', str(Tf))
    Tc = celsius(Tf)
    Tk = kelvin(Tc)
def celsius(Tf):
    Tc = 5 / 9 * (Tf - 32)
    print('The temperature in celsius is:', str(Tc))
    return Tc
def kelvin(Tc):
    Tk = Tc + 273.15
    print('The temperature in celsius is:', str(Tk))
    return Tk
convert_temp()