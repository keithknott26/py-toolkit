def list_of_months(start_month):
    """
    Make cycled list of months starting with given
    >>> list_of_months(3)
    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]

    >>> list_of_months(4)
    [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
    """
    start_month -= 1  # human months start with 1 not 0
    end_month = 12 + start_month
    months = [((month % 12) + 1) for month in range(start_month, end_month)]
    return months
