# BINOMIAL CALCULATOR

# SUBSCRIPT: \u208
# SUPERSCRIPT: \u00b

def fact(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact


def main():
    print("Binomial Expression: (x + y)\u207F\n")

    try:
        x = float(input("Enter the value for x [Press ENTER for DEFAULT]: "))
    except ValueError:
        x = 'a'
    try:
        y = float(input("Enter the value for y [Press ENTER for DEFAULT]: "))
    except ValueError:
        y = 'b'
    try:
        n = float(input("Enter the value for n [Press ENTER for DEFAULT]: "))
    except:
        n = 'n'

    if n == 'n':
        print(f"\nBinomial Expression: (x + y)\u207F = ({x} + {y})\u207F")
    else:
        print(f"\nBinomial Expression: (x + y)\u207F = ({x} + {y}) ^ {n}")


if __name__ == '__main__':
    main()
