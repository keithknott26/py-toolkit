def zipper(list_1, list_2):
    """
    Combining elements of two lists into one in zip fashion: first, first, second, second
    >>> zipper([1, 2, 3], [1, 2, 3])
    [1, 1, 2, 2, 3, 3]
    """
    zipped = []
    for temp_tuple in zip(list_1, list_2):
        for z in temp_tuple:
            zipped.append(z)
    return zipped