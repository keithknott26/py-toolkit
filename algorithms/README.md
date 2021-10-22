# DataStructures and Algorithms, in Python

This is a collection of code-snippets/notes created while studying Algorithms and Data Structures.

***

Table of Contents
====

* [01. Linear Search](#01-linear-search)
* [02. Binary Search](#02-binary-search)
* [03. Selection Sort](#03-selection-sort)
* [04. Recursion](#04-recursion)


***

## 01. Linear Search

### Introduction

Linear Search is an algorithm to search a data set for an element of interest. It is one of the many search algorithms available and is also the most direct and simple of the lot.

Linear search looks for the element of interest in a dataset starting from the first element and moves on to the consecutive elements till it finds the one we’re interested in. Due to this behaviour, it’s not the fastest search algorithm around.

In the worst case, when the element of interest is the last one (or near-last) in the data set, linear-search has to sift through till the last element. The larger the data set, the more iterations it takes to find the element of interest, in the worst case. Hence, the performance of Linear search takes a toll as the size of the data set grows.

Linear search works on a sorted or unsorted data set equally since it has to go through the elements one by one, and doesn’t mind if the data is ordered or not.

### Performance / Time Complexity

#### 1. Worst-case performance: O(n)

A worst-case analysis is done with the upper bound of the running time of the algorithm. ie.. the case when the maximum number of operations are executed.

The worst-case scenario for a linear search happens when the element-of-interest is not present in the dataset. A near worst-case scenario is when the element-of-interest is the last element of the dataset. In the first case, the search has to go through each element only to find that the element is not present in the dataset. In the second scenario, the search has to be done till the last element, which still takes iterations.

In the worst-case, the performance is O(n), where  n  is the number of elements in the dataset.

#### 2. Best-case performance: O(1)

In the best-case, where the element-of-interest is the first element in the dataset, only one search/lookup is needed. Hence the performance is denoted as O(1), for `n` elements.

#### 3. Average performance: O(n/2)

On an average, the performance can be denoted as O(n/2).

#### How does Linear search work?

1. Takes in a dataset as well as an element of interest.
2. Checks if the first element is the element of interest.
3. If yes, returns the element.
4. If not, move to the next element in the dataset.
5. Iterate till the dataset is exhausted.
6. Return  None if the element of interest is not present in the dataset.

##### Example 1:

```python
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
```

##### Example 2:

This is the same example as above, but with a little more information being printed out.

```python
def linear_search(my_list, item):
    """Linear search"""

    low_position = 0
    high_position = len(my_list) - 1

    print("\nDataset size : {0}".format(len(my_list)))
    print("Item of choice : {0}\n".format(item))

    while low_position < high_position:

        print("Searching at index {0} of the dataset".format(low_position))

        if my_list[low_position] == item:
            print("Your search item {0} is at position {1}".format(
                item, low_position))
            return low_position
        else:
            print("{0} is not at index {1}\n".format(item, low_position))
            low_position += 1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    linear_search(my_list, 16)
```

### Observations:

* Linear Search iterates through every element in the dataset until it finds the match.
* In Linear Search, the number of iterations grows linearly if the data set grows in size.
* This algorithm is called  Linear Search  due to this linear increase in the complexity depending on the dataset.
* The Best case is when the first iteration finds the element.
* The Worst case is when the element of interest is not present in the dataset.
* A very near worse case is when the element of interest is the last one in the dataset.

***

## 02. Binary Search

### Introduction

Binary Search is a search method used to find an object in a data set. This is much faster compared to the Linear Search algorithm we saw in a previous post.

This algorithm works on the Divide and Conquer principle. Binary Search gets its speed by essentially dividing the list/array in half in each iteration, thus reducing the data-set size for the next iteration.

Imagine searching for an element in a rather large dataset. Searching for an element one by one using Linear Search would take n iterations. In a worst case scenario, if the element being searched is not present in the dataset or is at the end of the dataset, the time taken to find the object/element would be proportional to the size of the dataset.

The element of interest is returned if it is present in the dataset, else a NULL/None value is.

***Note:***

* Binary search will only work effectively on a Sorted collection.

### Performance / Time Complexity

#### 1. Worst-case performance: log(n)

As discussed in the post on Linear Search, a worst-case analysis is done with the upper bound of the running time of the algorithm. ie.. the case when the maximum number of operations are needed/executed to find/search the element of interest in the dataset.

Of course, the worst-case scenario for any search algorithms is when the element of interest is not present in the dataset. The maximum number of searches has to be done in such a case, and it still ends up with no fruitful result. A similar but less worse-case is when the element is found in the final (or somewhere near the last) iteration.

Due to the divide-and-conquer method, the maximum number of iterations needed for a dataset of n elements is log(n), where the log base is 2.

Hence, for a data set of 10240 elements, Binary Search takes a maximum of 13 iterations.

```python
In [1]: import math

In [2]: math.log(10240, 2)
Out[2]: 13.321928094887364
```

For a data set of 50,000 elements, Binary Search takes 16 iterations in the worst case scenario while a Linear Search may take 50,000 iterations in a similar case.

```python
In [1]: import math

In [2]: math.log(50000, 2)
Out[2]: 15.609640474436812
```

ie.. the Worst case for Binary search takes log(n) iterations to find the element.


#### 2. Best-case performance: O(1)

The best case scenario is when the element of interest is found in the first iteration itself. Hence the best-case would be where the search finishes in one iteration.

ie.. The best-case scenario would be O(1).

#### 3. Average performance

[add notes]

### How does Binary Search work?

Imagine a sorted dataset of 100 numbers and we're searching for  98 is in the list. A simple search would start from index 0 , moves to the element at index 1, progresses element by element until the one in interest is found. Since we're searching for 98, it'll take n iterations depending on the number of elements between the first element in the dataset and 98.

Binary Search uses the following method, provided the dataset is sorted.

- Find the length of the data set.
- Find the lowest (index 0), highest (index n), and the middle index of the data set.
- Find the subsequent elements residing in the first, last, and middle index.
- Check if the element of interest is the middle-element.
- If not, check if the element-of-interest is higher or lower than the middle element.
- If it is higher, assuming the dataset is sorted in an increasing order, move the lower index to one above the middle index.
- If it is lower, move the highest index to one below the middle index.
- Check if the element of interest is the middle-element in the new/shorter dataset.
- Continue till the element of interest is found.


![Binary Search - Source: Wikipedia](https://github.com/arvimal/DataStructures-and-Algorithms-in-Python/blob/master/Images/Binary_Search.png  "Binary Search")

**Figure 1 : Binary Search - Source: Wikipedia**

The figure above shows how Binary Search works on a dataset of 16 elements, to find the element 7.

1. Index 0 , Index 16, and the middle index are noted.
2. Subsequent values/elements at these indices are found out as well.
3. Check if the element of interest 7 is equal to, lower, or higher than the middle element 14 at index 8.
4. Since it's lower and the dataset is sorted in an increasing order, the search moves to the left of the middle index, ie.. from index 0 to index 7.
5. The lower index is now 0, the higher index is now 7, and the middle index is now 3, the element in the middle index is 6.
6. Check if the element of interest 7 is lower or higher than the middle element 6 at index 3.
7. Since it's higher and the dataset is sorted in an increasing order, the search moves to the right of the middle index, ie.. from index 4 to index 7.
8. So on and so forth.. till we arrive at the element of interest, ie.. 7.

As noted eariler, the data set is divided into half in each iteration. A numeric representation on how Binary search progresses can be seen as:


***

100 elements -> 50 elements -> 25 elements -> 12 elements -> 6 elements - 3 elements -> 1 element

***

### Code

##### Example 1 : (Data set sorted in Increasing order)

```python
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
```

##### Example 2 : (Same as above, but with more statements explaining how it works)

```python
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
```

### Observations:

- Binary Search needs a Sorted dataset to work.
- It can work on datasets sorted in both increasing and decreasing order.
- Binary Search finds the element of interest in logarithmic time, hence is also known as Logarithmic Search.
- Binary Search searches through a dataset of n elements in log(n) iterations, in the worst case scenario.

### References:

1. [http://bigocheatsheet.com/](http://bigocheatsheet.com/)
2. [https://en.wikipedia.org/wiki/Binary_search_algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)
3. [http://quiz.geeksforgeeks.org/binary-search/](http://quiz.geeksforgeeks.org/binary-search/)
4. [https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/](https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/)
5. [http://research.cs.queensu.ca/home/cisc121/2006s/webnotes/search.html](http://research.cs.queensu.ca/home/cisc121/2006s/webnotes/search.html)


## 03. Selection Sort

### Introduction

Selection Sort is a sorting algorithm used to sort a data set either in incremental or decremental order.

It goes through the entire elements one by one and hence it's not a very efficient algorithm to work on large data sets.

### How does Selection sort work?

Selection sort starts with an un-sorted data set. With each iteration, it builds up a sub data-set with the sorted data.

By the end of the sorting process, the sub data-set contains the entire elements in a sorted order.

The steps can be described as following:

1. Iterate through the data set one element at a time.
2. Find the biggest element in the data set (Append it to another if needed)
3. Reduce the sample space by the biggest element just found. The new data set becomes `n - 1` compared to the previous iteration.
4. Start over the iteration again, on the reduced sample space.
5. Continue till we have a sorted data set, either incremental or decremental

### How does the data sample reduces in each iteration?

```bash
[10, 4, 9, 3, 6, 19, 8] 	- Data set
[10, 4, 9, 3, 6, 8] - [19] 	- After Iteration 1
[4, 9, 3, 6, 8] - [10, 19] 	- After Iteration 2
[4, 3, 6, 8] - [9, 10, 19] 	- After Iteration 3
[4, 3, 6] - [8, 9, 10, 19] 	- After Iteration 4
[4, 3] - [6, 8, 9, 10, 19] 	- After Iteration 5
[3] - [4, 6, 8, 9, 10, 19] 	- After Iteration 6
[3, 4, 6, 8, 9, 10, 19]  	- After Iteration 7 - Sorted data set
```

Let's check what the Selection Sort algorithm has to go through in each iteration


```bash
[10, 4, 9, 3, 6, 19, 8]		- Data set
[10, 4, 9, 3, 6, 8] 		- After Iteration 1
[4, 9, 3, 6, 8]			- After Iteration 2
[4, 3, 6, 8] 			- After Iteration 3
[4, 3, 6]			- After Iteration 4
[4, 3]				- After Iteration 5
[3]				- After Iteration 6
[3, 4, 6, 8, 9, 10, 19]		- After Iteration 7 - Sorted data set
```

### Performance / Time Complexity

Selection Sort has to go through all the elements in the data set, no matter what.

Hence, the Worst case, Best case and Average Time Complexity would be O(n^2).

Since `Selection Sort` takes in `n` elements while starting, and goes through the data set `n` times (each step reducing the data set size by 1 member), the iterations would be:

```bash
n + [ (n - 1) + (n - 2) + (n - 3) + (n - 4) + ... + 2 + 1 ]
```

We are more interested in the worse-case scenario. In a very large data set, an `n - 1`, `n - 2` etc.. won't make a difference.

Hence we can re-write the above iterations as:

```bash
n + [n + n + n + n ..... n]
```

Or also as:

```bash
n x n (n^2)
```

#### 1. Worst-case performance:

O(n^2)

#### 2. Best-case performance:

O(n^2)

#### 3. Average performance:

O(n^2)

### Code

##### Example 1

```python
def find_smallest(my_list):

    smallest = my_list[0]
    smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i
    return smallest_index

def selection_sort(my_list):
    new_list = []
    for i in range(len(my_list)):
        smallest = find_smallest(my_list)
        new_list.append(my_list.pop(smallest))
    return new_list
```

### Observations:

1.Selection Sort is an algorithm to sort a data set, but it is not particularly fast.

2.It takes `n` iterations in each step to find the biggest element in that iteration.

3.The next iteration has to run on a data set of `n - 1` elements comapred to the previous iteration.

4.For `n` elements in a sample space, Selection Sort takes `n x n` iterations to sort the data set.

#### References:
1. [https://en.wikipedia.org/wiki/Selection_sort](https://en.wikipedia.org/wiki/Selection_sort)
2. [http://bigocheatsheet.com/](http://bigocheatsheet.com/)


## 04. Recursion

### Introduction

Recursion is a technique where a function calls itself until a condition is met.

A typical example of recursion is a `factorial` function.

### How does Recursion work?

A recursion function calls itself, to reach

There is a `Base` case and a `Recursive` case.


### Performance / Time Complexity

#### 1. Worst-case performance:
#### 2. Best-case performance:
#### 3. Average performance:

###Code

##### Example 1:

* A `factorial` function in a `while` loop:

```python
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
```

* The same function above, in a `recursive` loop:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of {0} is {1}".format(10, factorial(10)))
print("Factorial of {0} is {1}".format(20, factorial(20)))
print("Factorial of {0} is {1}".format(30, factorial(30)))
print("Factorial of {0} is {1}".format(40, factorial(40)))
```

##### Example 2:

* A `sum` function in a normal loop


* The same `sum` function above, in a `recursive` loop.

```python
def sum(my_list):
    if my_list == []:
        return 0
    else:
        return my_list[0] + sum(my_list[1:])


print(sum([10, 23, 14, 12, 11, 94, 20]))
```

##### Code explanation

### Observations:

### References:

1.[Grokking Algorithms](http://www.amazon.in/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230/ref=sr_1_1?s=books&ie=UTF8&qid=1486811444&sr=1-1&keywords=grokking+algorithms)

2.[Data Structures and Algorithms in Python](https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/812656217X/ref=sr_1_1?ie=UTF8&qid=1487126103&sr=8-1&keywords=data+structures+and+algorithms+in+python)


----
----
Boilerplate:
## num. Algo/DS name

### Introduction

### How does Algo/DS-name work?

### Performance / Time Complexity

#### 1. Worst-case performance:
#### 2. Best-case performance:
#### 3. Average performance:

###Code

##### Example 1:
##### Code explanation
##### Example 2:

### Observations:

### References:

