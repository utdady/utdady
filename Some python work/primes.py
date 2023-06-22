"""A module demonstrating generator functions and related concepts."""

__author__ = "Aditya Bhaskar, adbhaska@ucsc.edu"


def is_prime(n):
    """ Returns whether n is prime. """
    for i in range(2, n):
        if not n % i:
            return False
    return True


def is_semiprime(n):
    num = prime_factors(n)
    if len(num) == 0:
        return False
    elif len(num) == 1:
        if num[0] * num[0] == n:
            return True
    elif len(num) == 2:
        if num[0] * num[1] == n:
            return True
    else:
        return False


def primes():
    """ Yields an infinite sequence of prime numbers, in ascending order. """
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1


def prime_factors(n):
    """ Returns a list of prime numbers with product n, in ascending order. """
    prime_list = []
    x = 2
    while True:
        if n % x == 0:
            if is_prime(x):
                n = n / x
                prime_list.append(x)
        else:
            x += 1
        if x > n:
            break
    return prime_list


def semiprimes():
    """ Yields an infinite sequence of semiprimes, in ascending order. """
    x = 0
    while True:
        if is_semiprime(x):
            yield x
        x += 1


def elements_under(sequence, bound, predicate=None):
    """Yields a finite sequence of elements under a given bound, optionally matching a predicate.
    :param sequence: an infinite sequence of integers, e.g. primes()
    :param bound: an exclusive upper bound for the yielded sequence
    :param predicate: an optional function used to select values from the sequence
    :yield: all elements from sequence comparing less than bound. If predicate is not None, only
    yields values for which predicate returns True"""
    elt = []
    for elts in sequence:
        if elts > bound - 1:
            break
        elt.append(elts)
    x = predicate
    y = list(filter(x, range(2, bound)))
    comp = list(sorted(set(elt).intersection(set(y))))
    for item in comp:
        yield item


def nth_element(sequence, n):
    """Returns the nth element of a possibly infinite sequence of integers.
    :param sequence: a sequence of integers, e.g. primes()
    :param n: the sequence index desired
    :return: the value at index n of the sequence"""
    elt = []
    count = 0
    for nums in sequence:
        elt.append(nums)
        count += 1
        if count > n:
            break
    return elt[n]
