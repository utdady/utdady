from time import perf_counter

# IMPORTANT NOTE: ITERATIVE is quicker.

#iterative method
def ifact(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact


def rfact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return(n * rfact(n - 1))


def main():
    num = int(input("Enter the number whose FACTORIAL is to be calculated: "))
    iterator = int(input("\nEnter the number of times you want to check the time: "))
    funcs = {ifact: 'Iterative Method', rfact: 'Recursive Method'}
    for func in funcs:
        time = 0
        cumulativeTime = 0
        for i in range(iterator):
            start = perf_counter()
            result = func(num)
            end = perf_counter()
            timer = end - start
            cumulativeTime += timer
        time = cumulativeTime / iterator
        print(f"Average Time for {funcs[func]}: {time}")
    print(f"The result is {result}.")


if __name__ == '__main__':
    main()

