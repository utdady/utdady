from timeit import timeit, Timer

def test1(n):
    for i in range(n * n):
        for j in range(n):
            print(n)

t1 = Timer("test1(3)", "from __main__ import test1")
print("test1: ", t1.timeit(number=1), "miliseconds")

def test2(n):
    for i in range(n * n):
        print(n)

t2 = Timer("test2(3)", "from __main__ import test2")
print("test1: ", t2.timeit(number=1), "miliseconds")
