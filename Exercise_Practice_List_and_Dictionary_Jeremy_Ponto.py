# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:27:08 2019

@author: user
"""

# Exercise 1
inventory = {
        'gold' : 500,
        'pouch' : [
                'flint',
                'twine',
                'gemstone'
                ],
        'backpack' : [
                'xylophone',
                'dagger',
                'bedroll',
                'bread loaf'
                ]
        }
print(inventory)
inventory['pocket'] = [
        'seashell',
        'strange berry',
        'lint'
        ]
print(inventory)
inventory['backpack'].sort()
print(inventory)
inventory['backpack'].remove('dagger')
print(inventory)
inventory['gold'] += 50
print(inventory)

# Exercise 2
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }
stocks = {
        "banana": 3,
        "apple": 0,
        "orange": 1,
        "pear": 2
        }
for item in prices:
    print(item + "\nprice: " + str(prices[item]) + "\nstock: " + str(stocks[item]))
total = 0
for item in prices:
    total += prices[item] * stocks[item]
print(total)

# Exercise 3
groceries = [
        "banana",
        "orange",
        "apple"
        ]
stocks = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
        } 
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }
def compute_bill(food):
    total = 0
    for item in food:
        if stocks[item] != 0:
            total += prices[item]
            stocks[item] -= 1
    return total
print(compute_bill(groceries))

# Exercise 4
eren = {
        "name": "Eren",
        "homework": [
                90.0,
                97.0,
                75.0,
                92.0
                ],
        "quizzes": [
                88.0,
                40.0,
                94.0
                ],
        "tests": [
                75.0,
                90.0
                ]
        }
mikasa = {
        "name": "Mikasa",
        "homework": [
                100.0,
                92.0,
                98.0,
                100.0
                ],
        "quizzes": [
                82.0,
                83.0,
                91.0
                ],
        "tests": [
                89.0,
                97.0
                ]
        }
armin = {
        "name": "Armin",
        "homework": [
                0.0,
                87.0,
                75.0,
                22.0
                ],
        "quizzes": [
                0.0,
                75.0,
                78.0
                ],
        "tests": [
                100.0,
                100.0
                ]
        }
students = [
        eren,
        mikasa,
        armin
        ]
for student in students:
    print(student)
def average(numbers):
    total = sum(numbers)
    total = float(total)
    average = total / len(numbers)
    return average
def get_average(student):
    homework = average(student["homework"]) * 0.1
    quiz = average(student["quizzes"]) * 0.3
    test = average(student["tests"]) * 0.6
    score = homework + quiz + test
    return score
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
score = get_average(eren)
print(score)
print(get_letter_grade(score))
score = get_average(mikasa)
print(score)
print(get_letter_grade(score))
score = get_average(armin)
print(score)
print(get_letter_grade(score))
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
class_average = get_class_average(students)
print(class_average)
print(get_letter_grade(class_average))