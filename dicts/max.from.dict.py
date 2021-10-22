def max_key_from_dict(stats: dict):
    """
    Finds all keys with maximal value, returns a list

    >>> max_key_from_dict({'a': 1000, 'b': 3000, 'c': 100, 'd': 3000})
    ['b', 'd']

    >>> max_key_from_dict({})
    []
    """
    result = []
    for key in stats:
        if stats[key] == max(stats.values()):
            result.append(key)
    return result


def max_key_from_dict_comprehension(stats: dict):
    """
    List comprehension to find all keys with maximal value

    >>> max_key_from_dict_comprehension({'a': 1000, 'b': 3000, 'c': 100, 'd': 3000})
    ['b', 'd']

    >>> max_key_from_dict_comprehension({})
    []
    """
    return [key for key in stats if stats[key] == max(stats.values())]


def first_max_key(stats: dict):
    """
    Finds the first key that has the maximal value
    >>> first_max_key({'a': 1000, 'b': 3000, 'c': 100, 'd': 3000})
    'b'

    >>> first_max_key({})
    """
    if stats:
        max_value = max(stats.values())
    for key in stats.keys():
        if stats[key] == max_value:
            return key


def max_from_dict(stats: dict):
    """
    Actually max() has key parameter, that we can get use of.
    I just don't get how this piece works.
    >>> max_from_dict({'a': 1000, 'b': 3000, 'c': 100, 'd': 5000})
    'd'
    """
    return max(stats, key=stats.get)


def max_key_dict_list(stats: dict):
    """
    >>> max_key_dict_list({'a': [1000, 3000], 'b': [3000, 100], 'c': [100, 5], 'd': [3000]})
    ['a', 'b', 'd']

    >>> max_key_dict_list({})
    []
    """
    #  Finding the maximal value in whole dictionary
    max_value = 0
    for value in stats.values():
        if max(value) > max_value:
            max_value = max(value)
    #  Getting the keys of maximal values into list
    max_keys = []
    for key, value in stats.items():
        if max(value) == max_value:
            max_keys.append(key)
    return max_keys

