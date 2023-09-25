# 1 disc -> 1 move.
# subsequents moves -> 2x+1


def hanoi(n, source, spare, target):
    if n == 1:
        print('Move a disc from', source, 'to', target)
    elif n == 0:
        return
    else:
        hanoi(n - 1, source, target, spare)
        print('Move a disc from', source, 'to', target)
        hanoi(n - 1, spare, source, target)


def main():
    n = int(input('Enter the number of discs: '))
    # source = int(input('Enter source pole: '))
    # spare = int(input('Enter spare pole: '))
    # target = int(input('Enter target pole: '))
    print("\n")
    hanoi(n, 1, 2, 3)


if __name__ == '__main__':
    main()
