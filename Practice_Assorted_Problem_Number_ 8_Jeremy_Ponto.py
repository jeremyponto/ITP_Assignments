# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:06:13 2019

@author: user
"""

lwords = ["I", "want", "to", "eat", "fried", "rice"]
print(lwords)
def find_longest_word(lwords):
    longest_length = 0
    for word in lwords:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length
print(find_longest_word(lwords))