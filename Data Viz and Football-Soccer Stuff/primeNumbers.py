class Primes:
    def __init__(self, number):
        self.number = number

    def isPrime(self):
        step = 0
        for i in range(2, self.number + 1):
            if self.number % i == 0:
                step += 1
        if step == 1:
            return True
        else:
            return False


def main():
    primes = []
    for i in range(1900, 2022):
        P = Primes(i)
        if P.isPrime():
            primes.append(i)

    print(primes)


main()
