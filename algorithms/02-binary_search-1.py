#!/usr/bin/env python3

# Binary Search Algorithm
# Example 1
# This deals with a dataset sorted in increased order.

# A Binary Search Algorithm searches an Array/List for an element.
# The Array/List has to be sorted in order to get Binary Search to work.
#
# https://www.youtube.com/watch?v=5xlIPT1FRcA
# https://www.youtube.com/watch?v=D5SrAga1pno

# Idea:
# Some sort of search algorithms are required to search/find elements we're
# interested in, from a data collection.

# Usually, a linear search will take `n` cycles in the worst case, if there are
# `n` elements in the collection. ie.. the Big O notation would be O(n).

# Binary search divides the collection into half in each iteration, and hence
# the search finishes much faster than a normal search.

# Due to this, Binary Search is also termed as `Divide-and-Conquer` algorithm.

# Binary Search gains more momentum in larger data sets due to it's
# logarithmic approach.

# For a list/collection of `n` items, the number of cycles to find the
# element of interest would be `log(n)`.

# Hence, searching a list of 1024 elements using binary search would, in the
# worst case, take a max of 10 cycles.

# In [1]: import math ; math.log(1024, 2)
# Out[1]: 10.0

# How does the Binary Search algorithm work?
# a) Calculate the lowest and highest position of the data set.
# b) Calculate the middle position from the low and high positions.
# c) Find the element in the middle position
# d) Compare our element-of-interest with the element in the middle position.

# e) We start with comparing the element-of-interest with the middle element.
# If the middle element matches our element-of-interest, the middle element
# is returned.
# f) If the element-of-interest is less than the middle element, our
# element-of-interest must lie in the lower half of the data set.
# Reduce `high_position` to `mid_position - 1` and continue with the
# new data set in the next iteration.
# g) If the element-of-interest is greater than the middle element, it must
# lie in the upper half of the data set.
# The `low_position` should be increased to be `mid_position + 1`, and we
# work on the new data set in the next iteration.
# h) The data set reduces in half with each iteration, and the search process
# is repeated on the lower or upper half of the array.

# In the example below, we have a list/collection `my_list`, and we're
# searching for the element `item`.


def binary_search(my_list, item):

    # Find and set the low and high positions of the data set
    # Note that these are not the values, but just positions.
    low_position = 0
    high_position = len(my_list) - 1

    # Ideally `low_position` is always lower than `high_position`,
    # no matter how the list shrinks in each iteration.
    # Hence, we use a `while` loop which is always `True` to the condition
    while low_position <= high_position:

        # Find the middle position from the low and high positions
        mid_position = (low_position + high_position) // 2

    # Find the element residing in the middle position of the data set.
        mid_element = my_list[mid_position]

    # Check if the middle element is our element-of-interest, ie.. `item`
    # If so, return the position of our element-of-interest.
        if mid_element == item:
            print("\nYour search item {0} is at index {1}".format(
                item, mid_position))
            return mid_element

    # Check if the middle element is a value higher than our element-of-interest.
    # If so, our element-of-interest falls *below* the middle element
    # Hence, we re-adjust the high_position to the middle position, thus
    # reducing the data set size by half.
        elif mid_element > item:
            high_position = mid_position - 1

    # Check if the middle element is lower than our element-of-interest.
    # If so, our element-of-interest falls *above* the middle element.
    # Hence, we re-adjust the low_position to the middle position, and
    # reduces the data set by half, as we did in the case above.
        else:
            low_position = mid_position + 1

    # Since these three conditions are in a `while True` loop, this gets
    # executed until the data set is reduced to a size where the
    # element-of-interest remains and is identified.

    # If the element-of-interest is not present in the data set, this code
    # returns None.
    return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    binary_search(my_list, 3)
