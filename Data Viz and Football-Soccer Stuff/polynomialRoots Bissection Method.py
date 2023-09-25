import numpy as np

def func(z):
    f = lambda x: [z[i] * (x ** i) for i in range(len(z))]
    return f

def samesign(a, b):
    return a * b > 0

def find(f, a, b, res, tol, thr):
    '''if np.sign(sum(f(a))) == np.sign(sum(f(b))):
        raise Exception("The scalars a and b do not bound a root")
    '''

    m = (a + b) / 2

    if np.abs(sum(f(m))) < tol:
        return m
    elif np.sign(sum(f(a))) == np.sign(sum(f(m))):
        return find(f, m, b, res, tol, thr)
    elif np.sign(sum(f(b))) == np.sign(sum(f(m))):
        return find(f, a, m, res, tol, thr)

if __name__ == '__main__':
    res, tol, thr = (10 ** -2), (10 ** -6), (10 ** -3)
    coeff = str(input("Enter the polynomial coefficients:\n"))
    inter = str(input("Enter the interval:\n"))
    x, y = [int(i) for i in coeff.split()], [int(i) for i in inter.split()]
    function = func(x)
    root = find(function, y[0], y[1], res, tol, thr)
    print(f"Root found at {root}.")
