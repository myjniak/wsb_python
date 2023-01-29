from itertools import accumulate, repeat


class CollatzBadNumberError(Exception):
    """Bad start number"""


def iterate(f, x):
    """return (x, f(x), f(f(x)), ...)"""
    return accumulate(repeat(x), lambda fx, _: f(fx))


def collatz_iter(x):
    if x <= 0:
        raise CollatzBadNumberError("Collatz conjecture not applicable for numbers <=0")
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 + 1


def take_until_1(it):
    for x in it:
        yield x
        if x == 1:
            break


def collatz_conjecture(starting_number: int):
    """https://en.wikipedia.org/wiki/Collatz_conjecture
    https://www.youtube.com/watch?v=094y1Z2wpJg
    """
    return [n for n in take_until_1(iterate(collatz_iter, starting_number))]

