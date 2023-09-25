from time import perf_counter

# IMPORTANT NOTE : ITERATIVE is quicker.

def rfibo(n):
    first = 0
    second = 1
    
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return (ifibo(n-1) + ifibo(n-2))


def ifibo(n):
    first = 0
    second = 1

    for i in range(n-2):
        third = first + second
        first = second
        second = third
    return third


def main():
    num = int(input("Enter the NUMBER [OUTPUT WILL BE THE Nth FIBONACCI NUMBER]: "))
    iterator = int(input("\nEnter the number of times you want to check the time: "))
    funcs = {ifibo: 'Iterative Method', rfibo: 'Recursive Method'}
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
