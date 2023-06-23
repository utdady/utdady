'''
Prompt: Write a decorator function @calculate_time that calculates the time
        required for a function to run. For example, you can use the function
        sum1 as an input function for your decorator.
'''
from time import time

# Decorator:
def calculate_time(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"It took {(t2 - t1)} sec.")
        return result
    return wrap


@calculate_time
def sum1(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


if __name__ == '__main__':
    n = 1000000
    s = sum1(1000000)
    print(f'The sum of numbers from 1 to {n} is {s}.')
