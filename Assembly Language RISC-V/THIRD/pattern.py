done = False
while not done:
    n = int(input("Enter the height of the pattern (must be greater than 0):"))
    if n > 0:
        break
    else:
        print("Invalid Entry!")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
