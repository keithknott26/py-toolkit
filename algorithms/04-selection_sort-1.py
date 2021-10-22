#!/usr/bin/env python3

# Selection Sort
# Example 1

# Selection Sort is a sorting algorithm used to sort a data set either in
# incremental or decremental order.

# How does Selection sort work?

# 1. Iterate through the data set one element at a time.
# 2. Find the biggest element in the data set (Append it to another if needed)
# 3. Reduce the sample space to `n - 1` by the biggest element just found.
# 4. Start the iteration over again, on the reduced sample space.
# 5. Continue till we have a sorted data set, either incremental or decremental


# How does the data sample reduces in each iteration?
# [10, 4, 9, 3, 6, 19, 8] 		- Data set
# [10, 4, 9, 3, 6, 8] - [19] 	- After Iteration 1
# [4, 9, 3, 6, 8] - [10, 19] 	- After Iteration 2
# [4, 3, 6, 8] - [9, 10, 19] 	- After Iteration 3
# [4, 3, 6] - [8, 9, 10, 19] 	- After Iteration 4
# [4, 3] - [6, 8, 9, 10, 19] 	- After Iteration 5
# [3] - [4, 6, 8, 9, 10, 19] 	- After Iteration 6
# [3, 4, 6, 8, 9, 10, 19]  		- After Iteration 7 - Sorted data set

# Let's check what the Selection Sort algorithm has to go through in each
# iteration
# [10, 4, 9, 3, 6, 19, 8]	- Data set
# [10, 4, 9, 3, 6, 8] 		- After Iteration 1
# [4, 9, 3, 6, 8]			- After Iteration 2
# [4, 3, 6, 8] 				- After Iteration 3
# [4, 3, 6]					- After Iteration 4
# [4, 3]					- After Iteration 5
# [3] 						- After Iteration 6
# [3, 4, 6, 8, 9, 10, 19] 	- After Iteration 7 - Sorted data set

# Observations:
# 1. It takes `n` iterations in each step to find the biggest element.
# 2. The next iteration has to run on a data set of `n - 1` elements.
# 3. Hence the total number of overall iterations would be:
# n + (n - 1) + (n - 2) + (n - 3) + ..... 3 + 2 + 1

# Since `Selection Sort` takes in `n` elements while starting, and goes through
# the data set `n` times (each step reducing the data set size by 1 member),
# the iterations would be:

# n + [ (n - 1) + (n - 2) + (n - 3) + (n - 4) + ... + 2 + 1 ]

# Efficiency:
# We are interested in the worse-case scenario.
# In a very large data set, an `n - 1`, `n - 2` etc.. won't make a difference.

# Hence, we can re-write the above iterations as:
# n + [n + n + n + n ..... n]
# Or also as:
# n x n = n**2
# O(n**2)

# Final thoughts:
# Selection Sort is an algorithm to sort a data set, but it is not particularly
# fast. For `n` elements in a sample space, Selection Sort takes `n x n`
# iterations to sort the data set.

def find_smallest(my_list):
    smallest = my_list[0]
    smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list(i) < smallest:
            smallest = my_list(i)
            smallest_index = i
    return smallest_index


def selection_sort(my_list):
    new_list = []
    for i in range(len(my_list)):
        smallest = find_smallest(my_list)
        new_list.append(my_list.pop(smallest))
    return new_list


print(selection_sort([10, 12, 9, 4, 3, 6, 100]))
