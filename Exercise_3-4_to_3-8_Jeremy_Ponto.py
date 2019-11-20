# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:20:24 2019

@author: user
"""
# Page 46

# 3-4
guest_list = ['Bryan', 'Aric', 'Nicholas']
print(guest_list[0] + '\nYou are invited to dinner.')
print(guest_list[1] + '\nYou are invited to dinner.')
print(guest_list[2] + '\nYou are invited to dinner.')

# 3-5
guest_list = ['Bryan', 'Aric', 'Nicholas']
print(guest_list[2])
guest_list[2] = 'Kevin'
print(guest_list[0] + '\nYou are invited to dinner.')
print(guest_list[1] + '\nYou are invited to dinner.')
print(guest_list[2] + '\nYou are invited to dinner.')

# 3-6
guest_list = ['Bryan', 'Aric', 'Nicholas']
print('New dinner table found.')
guest_list.insert(0, 'Gardyan')
guest_list.insert(2, 'Jason')
guest_list.append('Kevin')
print(guest_list[0] + '\nYou are invited to dinner.')
print(guest_list[1] + '\nYou are invited to dinner.')
print(guest_list[2] + '\nYou are invited to dinner.')
print(guest_list[3] + '\nYou are invited to dinner.')
print(guest_list[4] + '\nYou are invited to dinner.')
print(guest_list[5] + '\nYou are invited to dinner.')

# 3-7
print('Two slots available for dinner.')
popped_guest_list = guest_list.pop()
print('Sorry ' + popped_guest_list + ', only two slots available for dinner.')
popped_guest_list_2 = guest_list.pop()
print('Sorry ' + popped_guest_list_2 + ', only two slots available for dinner.')
popped_guest_list_3 = guest_list.pop()
print('Sorry ' + popped_guest_list_3 + ', only two slots available for dinner.')
popped_guest_list_4 = guest_list.pop()
print('Sorry ' + popped_guest_list_4 + ', only two slots available for dinner.')
print(guest_list[0] + '\nYou are still invited to dinner.')
print(guest_list[1] + '\nYou are still invited to dinner.')
del guest_list[0]
del guest_list[0]
print(guest_list)

# Page 50

# 3-8
places_wish_list = ['Pisa', 'Colosseum', 'Eiffel Tower', 'Big Ben', 'London Bridge']
print(places_wish_list)
print(sorted(places_wish_list))
print(places_wish_list)
print(sorted(places_wish_list, reverse = True))
print(places_wish_list)
places_wish_list.reverse()
print(places_wish_list)
places_wish_list.reverse()
print(places_wish_list)
places_wish_list.sort()
print(places_wish_list)
places_wish_list.sort(reverse = True)
print(places_wish_list)