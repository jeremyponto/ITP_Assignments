# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:50:47 2019

@author: user
"""

# 1
def List(List = []):
    New_List = []
    for element in List:
        element = str(element)
        New_List.append(element)
    print(New_List)
    print(tuple(New_List))
List([3, 5, 7, 23])

# 2
def translate(text):
    vowels = ['a', 'i', 'u', 'e', 'o', ' ']
    letters = ""
    for letter in text:
        if letter in vowels:
            letters = letters + letter
        else:
            letters = letters + letter + 'o' + letter
    print(letters)
translate("this is fun")