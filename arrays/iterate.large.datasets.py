#!/usr/bin/env python

# Use generators to avoid crashed in memory when needed to interate on large set of data

# Generators can be built with the syntax of list comprehensions but inside ()
names = ['Tim', 'Mark', 'Donna', 'Albert', 'Sara']
gen_a = (len(n) for n in names)

print(next(gen_a))
print(next(gen_a))


# You define a generator function, using the yield keyword to return a value
def my_generator():
    names = ['Gianluca', 'Lisa', 'Sofia', 'Giulia']
    for i in names:
        yield i


# You define a generator iterator as an instance of the function
gen = my_generator()

# You call next to generate the next value
print(next(gen))
print(next(gen))

# Being the generator an iterator you can use it in a for loop as well
# notes that we keep generating from where we left
for val in gen:
    print(val)

# Remember: generators are used to generate the next value,
# they allow you to iterate over values without having to load them
# in memory. That's a key difference from a function where you
# only get a chance to return all results all at the same time.
# For example:
# 1. when you read a file the built in mechanism is a generator
# 2. the xrange uses a generator

# yield: what it does is save the "state" of a generator function
