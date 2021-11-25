#!/usr/bin/env python

"""
    Decorators are a special kind of function, a kind of function that takes one
    function object as an argument, and returns another function object as a result.

    Where do decorators come from?
    Some are built in in the language (i.e. @classmethod, @property) or built-in in the
    framework you want to use (@route in Flask). But you can/should also write them,
    just in the same way that you write other function definitions.

    Notes:
    Bear in mind that the wrapper function must have the same signature as the decorated function.
    To be able to decorate any function, the template wrapper takes *args and **kwarg parameters.

"""

import random


def simple_decorator(func):
    """
        Decorators allow you to wrap pre/post code to an existing function
    """
    def wrapper(*args, **kwargs):
        print("Decorator pre function call")
        ret_val = func(*args, **kwargs)
        print("Decorator post function call")
        return ret_val
    return wrapper


def retry(func):
    """
        Use of a decorator to retry a function execution (i.e polling a status)
    """
    def wrapper(*args, **kwargs):
        MAX_TRIES = 100
        tried = 0
        while True:
            response = func(*args, **kwargs)
            if response is False and tried < MAX_TRIES:
                print("Got False, decorator will retry for you")
                tried += 1
                continue
            break
        # wrapper need to return the funct value
        return response
    return wrapper


# Decorated functions


@simple_decorator
def foo(number):
    print("foo got a number {}".format(number))


@retry
def give_me_true():
    return random.choices([True, False]).pop()


# Testing
foo(500)
print(give_me_true())
