# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:03:20 2019

@author: user
"""

a = [1, 2, 3]
def is_member(x, a):
    for i in a:
        if i == x:
            return True
    return False
print(is_member(3, a))
print(is_member(4, a))