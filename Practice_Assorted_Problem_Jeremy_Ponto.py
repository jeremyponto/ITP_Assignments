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

# 3
import calendar
year_month = [2019, 11]
print(calendar.month(year_month[0], year_month[1], w=0, l=0))

# 4
a = [1, 2, 3]
def is_member(x, a):
    for i in a:
        if i == x:
            return True
    return False
print(is_member(3, a))
print(is_member(4, a))

# 5
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
    return False
print(overlapping(lst1, lst2))

# 6
def histogram(lst):
    for element in lst:
        print('*' * element)
histogram([4, 9, 7])

# 7
word_list = ["I", "want", "to", "eat", "fried", "rice"]
print(word_list)
length_list = []
for word in word_list:
    length_list.append(len(word))
print(length_list)

# 8
lwords = ["I", "want", "to", "eat", "fried", "rice"]
print(lwords)
def find_longest_word(lwords):
    longest_length = 0
    for word in lwords:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length
print(find_longest_word(lwords))

# 9
lwords = ["I", "want", "to", "eat", "fried", "rice"]
print(lwords)
def filter_long_word(lwords):
    new_lwords = []
    n = 3
    for word in lwords:
        if len(word) > n:
            new_lwords.append(word)
    return new_lwords
print(filter_long_word(lwords))