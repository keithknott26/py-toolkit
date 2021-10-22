import functools
import random
from datetime import datetime


def get_num():
    return format(random.randint(20, 255), 'X')


def timeit(msg=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()
            diff = end - start
            log_msg = f'Spent {diff.microseconds} microseconds in {func.__name__}. Msg:{msg}'
            print(log_msg)
            return result

        return wrapper

    return decorator


@timeit()
def generate_mac_old():
    return ':'.join([get_num() for _ in range(6)])


@timeit()
def generate_mac_new():
    return ':'.join((x() for x in [get_num] * 6))


def generate_mac_2():
    # f = [get_num for _ in range(6)]
    # f = [get_num, get_num, get_num, get_num, get_num, get_num]
    f = [get_num] * 6
    return ':'.join(x() for x in f)


def generate_mac_4():
    f = [get_num] * 6
    return [x() for x in f]


def generate_mac_5():
    return [f'{x}' for (_, x) in zip(range(6), get_num())]


if __name__ == '__main__':
    # print(generate_mac_old())
    # print(generate_mac_new())
    # print(generate_mac_new())
    # print(generate_mac_old())
    # print(generate_mac_2())
    # print(generate_mac_4())
    print(generate_mac_5())