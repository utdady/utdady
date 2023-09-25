def modifier(A):
    B = [x + y for x, y in zip(A, A[1:] + [A[0]])]
    print(B[0: len(A) - 1])

if __name__ == '__main__':

    modifier([1,3,2,4])
