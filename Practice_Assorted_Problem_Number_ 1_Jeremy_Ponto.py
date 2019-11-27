# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:59:25 2019

@author: user
"""

data = input("")
data = data.replace(",", "")
new_list = data.split()
print("List :", new_list)
print("Tuple :", tuple(new_list))