# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:00:35 2019

@author: user
"""

def translate(text):
    vowels = ['a', 'i', 'u', 'e', 'o', ' ']
    letters = ""
    for letter in text:
        if letter in vowels:
            letters += letter
        else:
            letters += letter + 'o' + letter
    print(letters)
translate("this is fun")