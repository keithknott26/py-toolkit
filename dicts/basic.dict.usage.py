import random
import sys
import os

super_villains = { 'Fiddler' : 'Mark Rondon',
                  'Black Panther' : 'Leonardo Vinci',
                  'Kali' : 'Joey Unart',
                  'Iron Man' : 'Robert Downey Jr.',
                   'Captain Cold' : 'Steven Kabbler'}


print(super_villains['Kali'])
print(len(super_villains))
del super_villains['Fiddler']
print(len(super_villains))
print(super_villains.keys())
print(super_villains.values())
