# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:03:52 2019

@author: user
"""

lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
    return False
print(overlapping(lst1, lst2))