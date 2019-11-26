# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:35:47 2019

@author: user
"""

# 2
no1 = float(input("Number 1= "))
no2 = float(input("Number 2= "))
no3 = float(input("Number 3= "))
def max_of_three(no1, no2, no3):
    if no1 > no2 and no1 > no3:
        return no1
    elif no2 > no1 and no2 > no3:
        return no2
    else:
        return no3
largest_number = max_of_three(no1, no2, no3)
print("Largest number= ", largest_number)

# 6
def is_palindrome():
    word = "Radar"
    word_reversed = reversed(word)
    return word == word_reversed
palindrome = is_palindrome()
print(palindrome)

# 7
def palindrome_recognizer():
    phrases = ["Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", "Dammit, I'm mad!"]
    for phrase in phrases:
        phrase = phrase.replace(" ", "")
        phrase = phrase.replace("'", "")
        phrase = phrase.replace(".", "")
        phrase = phrase.replace("?", "")
        phrase = phrase.replace(",", "")
        phrase = phrase.replace("!", "")
        print(list(phrase.lower()) == list(reversed(phrase.lower())))    
palindrome_recognizer()