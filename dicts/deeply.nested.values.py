"""access deeply nested values in dictionary"""

example_dict = {'very': {'deeply': {'nested': {'value': 100}}}}


def using_dotmap_module(dict_):
    """
    >>> using_dotmap_module(example_dict)
    100
    """
    from dotmap import DotMap
    dict_with_dots = DotMap(dict_)
    value = dict_with_dots.very.deeply.nested.value
    return value


def using_jsonpath(dict_):
    """
    >>> using_jsonpath(example_dict)
    100
    """
    from jsonpath import jsonpath
    value = jsonpath(dict_, '$.very.deeply.nested.value')
    return value[0]



