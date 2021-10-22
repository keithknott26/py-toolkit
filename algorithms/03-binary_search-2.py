#!/usr/bin/env python3

# Binary Search
# Example 2
# This deals with a dataset sorted in increased order.


def binary_search(my_list, item):

    # Find and set the low and high positions of the data set
    # Note that these are not the values, but just positions.
    low_position = 0
    high_position = len(my_list) - 1

    # Calculate the Complexity
    import math
    complexity = math.ceil(math.log(len(my_list), 2))

    # Print some info on the dataset
    print("\nDataset size : {0} elements".format(len(my_list)))
    print("Element of interest : {0}".format(item))
    print("Maximum number of iterations to find {0} : {1}\n".format(
        item, complexity))

    # Ideally `low_position` is always lower than `high_position`,
    # no matter how the list shrinks in each iteration.
    # Hence, we use a `while` loop which is always `True` to the condition

    while low_position <= high_position:

        # Find the middle position from the low and high positions
        mid_position = (low_position + high_position) // 2

    # Find the element residing in the middle position of the data set.
        mid_element = my_list[mid_position]

        print("Element at min index : {0}".format(my_list[low_position]))
        print("Element at max index : {1}".format(
            high_position, my_list[high_position]))
        print("Element at mid index {0} : {1}".format(
            mid_position, mid_element))

    # Check if the middle element is our element-of-interest, ie.. `item`
    # If so, return the position of our element-of-interest.
        if mid_element == item:
            print("\nYour search item {0} is at index {1}".format(
                item, mid_position))
            return mid_element

    # Check if the middle element is a value higher than our
    # element-of-interest.
    # If so, our element-of-interest falls *below* the middle element
    # Hence, we re-adjust the high_position to the middle position, thus
    # reducing the data set size by half.
        elif mid_element > item:
            high_position = mid_position - 1
            print("{0} in the left subset, omitting the right subset\n".format(item))

    # Check if the middle element is lower than our element-of-interest.
    # If so, our element-of-interest falls *above* the middle element.
    # Hence, we re-adjust the low_position to the middle position, and
    # reduces the data set by half, as we did in the case above.
        else:
            low_position = mid_position + 1
            print("{0} in the right subset, omitting the left subset\n".format(item))

    # Since these three conditions are in a `while True` loop, this gets
    # executed until the data set is reduced to a size where the
    # element-of-interest remains and is identified.

    # If the element-of-interest is not present in the data set, this code
    # returns None.
    print("Element of interest not in dataset\n")
    return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    binary_search(my_list, 13)
