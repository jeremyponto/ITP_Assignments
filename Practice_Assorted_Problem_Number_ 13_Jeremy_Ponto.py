# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:10:25 2019

@author: user
"""

verbs = ["try", "brush", "run", "fix"]
def makeForms(verbs):
    new_verbs = []
    for verb in verbs:
        if verb[-1:] == 'y':
            new_verbs.append(verb[:-1] + "ies")
        elif verb[-1:] in ['o', 's', 'x', 'z'] or verb[-2:] in ["ch", "sh"]:
            new_verbs.append(verb + "es")
        else:
            new_verbs.append(verb + 's')
    print(new_verbs)
makeForms(verbs)