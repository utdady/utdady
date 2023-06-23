def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def check(listt):
    for i in range(len(listt)):
        for j in range(len(listt)):
            if i != j:
                vert = abs(listt[i] - listt[j])
                hori = abs((i + 1) - (j + 1))
                if vert == hori:
                    return False
    return True

if __name__ == '__main__':
    num = int(input('Enter the number of queens:\n'))
    data = [i+1 for i in range(num)]

    perms = []
    for i in all_perms(data):
        perms.append(i)

    sol = []
    for i in perms:
        if check(i):
            sol.append(i)
    print(f'The {num}-queens puzzle has {len(sol)} solutions:')
    for i in sol:
        print(i)
