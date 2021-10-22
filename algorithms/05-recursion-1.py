#!/usr/bin/env python3

# Recursion
# Example 1

"""
An example of a factorial function in a `while` loop

def fact(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n = n - 1
    return factorial

print("Factorial of {0} is {1}".format(10, fact(10)))
print("Factorial of {0} is {1}".format(20, fact(20)))
print("Factorial of {0} is {1}".format(30, fact(30)))
print("Factorial of {0} is {1}".format(40, fact(40)))
"""


def factorial(n):
    """
    The same function above, in a recursive loop
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of {0} is {1}".format(10, factorial(10)))
print("Factorial of {0} is {1}".format(20, factorial(20)))
print("Factorial of {0} is {1}".format(30, factorial(30)))
print("Factorial of {0} is {1}".format(40, factorial(40)))

