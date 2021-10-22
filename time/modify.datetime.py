from datetime import datetime, timezone, timedelta


def get_seconds_until(date_in_iso):
    """
    Gets seconds from current time to the date in iso format
    If date is in the past value will be negative
    """
    time_pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
    if '.' not in date_in_iso:
        time_pattern = '%Y-%m-%dT%H:%M:%SZ'
    future = datetime.strptime(date_in_iso, time_pattern)
    now = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    diff = future - now
    return int(diff.total_seconds())


def get_date_from_now_seconds(seconds=0, *, minutes=0, hours=0, days=0):
    """
    Creates a string with date in '2020-05-09T01:16:22Z' format

    :param seconds: int
    :param minutes: int
    :param hours: int
    :param days: int
    :return: str
    """
    today = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    new_date = today + timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
    return new_date.isoformat(timespec='seconds') + 'Z'


def get_date_from_now_microseconds(seconds=0.0, *, minutes=0, hours=0, days=0):
    """
    Creates a string with date in '2020-05-09T01:16:22Z' format

    >>> '.' not in get_date_from_now_microseconds(1)
    True

    >>> '2020-05-09T01:16:22.1Z'[-3:] in get_date_from_now_microseconds(0.1)
    True

    >>> '2020-05-09T01:16:22.01Z'[-4:] in get_date_from_now_microseconds(0.01)
    True

    >>> '2020-05-09T01:16:22.001Z'[-5:] in get_date_from_now_microseconds(0.001)
    True

    >>> '2020-05-09T01:16:22.0001Z'[-6:] in get_date_from_now_microseconds(0.0001)
    True

    >>> '2020-05-09T01:16:22.00001Z'[-7:] in get_date_from_now_microseconds(0.00001)
    True

    >>> '.' not in get_date_from_now_microseconds(0.000001)
    True
    """
    today = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    new_date = today + timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
    iso_new_date = new_date.isoformat(timespec='microseconds')
    _, microseconds = iso_new_date.split('.')
    microseconds = float(f'.{microseconds}')
    microseconds = f'{microseconds:.5f}'.rstrip('0').rstrip('.')
    return new_date.isoformat(timespec='seconds') + microseconds + 'Z'


def get_date_from_now_milliseconds(seconds=0.0, *, milliseconds=0, minutes=0, hours=0, days=0):
    """
    Create date-time string in Cinarra format

    :param seconds: float
    :param milliseconds: int
    :param minutes: int
    :param hours: int
    :param days: int
    :return: str

    >>> '.' not in get_date_from_now_milliseconds(1)
    True

    >>> '2020-05-09T01:16:22.1Z'[-3:] in get_date_from_now_milliseconds(0.1)
    True

    >>> '2020-05-09T01:16:22.01Z'[-4:] in get_date_from_now_milliseconds(0.01)
    True

    >>> '2020-05-09T01:16:22.001Z'[-5:] in get_date_from_now_milliseconds(0.001)
    True

    >>> get_date_from_now_milliseconds(0.001) == get_date_from_now_milliseconds(milliseconds=1)
    True

    >>> '.' not in get_date_from_now_milliseconds(0.0001)
    True
    """
    today = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    new_date = today + timedelta(milliseconds=milliseconds, seconds=seconds, minutes=minutes, hours=hours, days=days)
    iso_new_date = new_date.isoformat(timespec='milliseconds')
    _, milliseconds = iso_new_date.split('.')
    milliseconds = float(f'.{milliseconds}')
    milliseconds = str(milliseconds).lstrip('0') if milliseconds else ''
    return new_date.isoformat(timespec='seconds') + milliseconds + 'Z'


def is_iso_date(date_in_iso):
    """Checks whether the given date matches the Cinarra format"""
    time_pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
    if '.' not in date_in_iso:
        time_pattern = '%Y-%m-%dT%H:%M:%SZ'
    try:
        datetime.strptime(date_in_iso, time_pattern)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()


