# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:14:33 2019

@author: user
"""

alphabets = []
sentence = str(input(""))
sentence = sentence.casefold()
rot = int(input(""))
new_alphabets = []
def init_list(alphabets):
    for i in range(97, 123, 1):
        alphabets.append(chr(i))
def init_shifted_list(rot):
    x = 0
    for i in range(97, 123, 1):
        x = i + rot
        if x > 122:
            x = x - 26
        new_alphabets.append(chr(x))
def encoder(sentence):
    new_sentence = ""
    for i in sentence:
        if i in alphabets:
            new_sentence += new_alphabets[alphabets.index(i)]
        else:
            new_sentence += i
    return new_sentence
def decoder(new_sentence):
    sentence = ""
    for i in new_sentence:
        if i in alphabets:
            sentence += alphabets[alphabets.index(i)]
        else:
            sentence += i
    return sentence
init_list(alphabets)
init_shifted_list(rot)
print(new_alphabets)
print(encoder(sentence))
print(decoder(new_sentence))