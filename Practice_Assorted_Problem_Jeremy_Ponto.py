# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:50:47 2019

@author: user
"""

# 1
data = input("")
data = data.replace(",", "")
new_list = data.split()
print("List :", new_list)
print("Tuple :", tuple(new_list))

# 2
def translate(text):
    vowels = ['a', 'i', 'u', 'e', 'o', ' ']
    letters = ""
    for letter in text:
        if letter in vowels:
            letters += letter
        else:
            letters += letter + 'o' + letter
    print(letters)
translate("this is fun")

# 6
def histogram(lst):
    for element in lst:
        print('*' * element)
histogram([4, 9, 7])

# 7
word_list = ["saya", "mau", "makan", "nasi", "goreng"]
print(word_list)
length_list = []
for word in word_list:
    length_list.append(len(word))
print(length_list)

# 8
lwords = ["saya", "mau", "makan", "nasi", "goreng"]
print(lwords)
def find_longest_word(lwords):
    longest_length = 0
    for word in lwords:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length
print(find_longest_word(lwords))

# 9
lwords = ["saya", "mau", "makan", "nasi", "goreng"]
print(lwords)
def filter_long_word(lwords):
    new_lwords = []
    n = 4
    for word in lwords:
        if len(word) > n:
            new_lwords.append(word)
    return new_lwords
print(filter_long_word(lwords))