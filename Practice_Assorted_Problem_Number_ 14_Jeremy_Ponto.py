# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:11:18 2019

@author: user
"""

def makeForming():
    verbs = ["go", "lie", "see", "move", "hug"]
    new_verbs = []
    for verb in verbs:
        if verb[-1:] == 'e' and verb[-2:] != "ie" and verb not in ["be", "see", "flee", "knee"]:
            new_verbs.append(verb[:-1] + "ing")
        elif verb[-2:] == "ie":
            new_verbs.append(verb[:-2] + "ying")
        elif verb[-3:-2] and verb [-1:] not in ['a', 'i', 'u', 'e', 'o'] and verb[-2:-1] in ['a', 'i', 'u', 'e', 'o']:
            new_verbs.append(verb + verb[-1] + "ing")
        else:
            new_verbs.append(verb + "ing")
    print(new_verbs)
makeForming()