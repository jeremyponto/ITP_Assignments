# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:14:33 2019

@author: user
"""

import string
alphabets = string.ascii_lowercase
sentence = str(input(""))
sentence = sentence.casefold()
shift = int(input(""))
def encoder(sentence):
    new_sentence = ""
    for letter in sentence:
        i = alphabets.index(letter) + shift
        if i >= 26:
            i = i % 26
        new_sentence += alphabets[i]
    return new_sentence
def decoder(new_sentence):
    sentence = ""
    for letter in new_sentence:
        i = alphabets.index(letter) - shift
        if i == 0:
            i = i + 26 - shift
        sentence += alphabets[i]
    return sentence
new_sentence = encoder(sentence)
print(new_sentence)
print(decoder(new_sentence))