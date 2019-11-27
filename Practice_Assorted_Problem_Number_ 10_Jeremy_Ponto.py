# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:07:51 2019

@author: user
"""

sentence = "The quick brown fox jumps over the lazy dog"
sentence = sentence.casefold()
sentence = sentence.replace(" ", "")
def pangram(sentence):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in sentence:
        if letter in alphabets:
            alphabets.remove(letter)
    if len(alphabets) == 0:
        print("pangram")
    else:
        print("not pangram")
pangram(sentence)