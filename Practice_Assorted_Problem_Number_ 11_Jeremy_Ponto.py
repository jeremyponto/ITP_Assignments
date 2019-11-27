# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:09:14 2019

@author: user
"""

string = "I want to eat fried rice"
string = string.casefold()
def char_freq(string):
    freq_list = {}
    for char in string:
        if char in freq_list:
            freq_list[char] += 1
        else:
            freq_list[char] = 1
    print(freq_list)
char_freq(string)