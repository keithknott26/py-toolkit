import random
import sys
import os

grocery_list =['Juice','Potatoes','Tomatoes','Carrots','Pickles']

print(grocery_list[0])

grocery_list[0]='Green Juice'

print(grocery_list[0])

print(grocery_list[1:3])
other_events =['Wash a Car','Pick up','Cash check']

to_do_list = [other_events , grocery_list]
print(to_do_list)
print(to_do_list[1][3])

grocery_list.append('Onions')
print(grocery_list)
grocery_list.insert(1 , "Bananas")
print(grocery_list)

to_do_list2 = grocery_list + to_do_list
print(to_do_list2)
print(len(to_do_list2))