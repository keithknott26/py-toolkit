#!/usr/bin/env python3

# Linear Search Algorithm
# Example 1

# https://en.wikipedia.org/wiki/Linear_search
# Worst-case performance : O(n)
# Best-case performance	: O(1)
# Average-case performance : O(n/2)


def linear_search(my_list, item):
    """Linear search"""

    low_position = 0
    high_position = len(my_list) - 1

    while low_position < high_position:

        if my_list[low_position] == item:
            print("Your search item {0} is at position {1}".format(
                item, low_position))
            return low_position
        else:
            low_position += 1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    linear_search(my_list, 5)
