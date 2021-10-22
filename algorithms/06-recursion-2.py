#!/usr/bin/env python3

# Recursion
# Example 2

"""
An example of a sum function in an `if` loop

def sum(my_list):
    num = 0
    for i in my_list:
        num += i
    return num


print(sum([10, 23, 14, 12, 11, 94, 20]))
"""


def sum(my_list):
    """
    The same `sum` function using recursion
    """
    if my_list == []:
        return 0
    else:
        return my_list[0] + sum(my_list[1:])


print(sum([10, 23, 14, 12, 11, 94, 20]))
"""