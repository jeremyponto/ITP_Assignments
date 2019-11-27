# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:06:21 2019

@author: user
"""

lwords = ["I", "want", "to", "eat", "fried", "rice"]
print(lwords)
def filter_long_word(lwords):
    new_lwords = []
    n = 3
    for word in lwords:
        if len(word) > n:
            new_lwords.append(word)
    return new_lwords
print(filter_long_word(lwords))