def permute(items, level):
    for i in range(level):
        yield items
        items.append('')
        items[-1] = items[0]
        items.remove(items[0])

def Rpermute(items, level):
    if level > 0:
        print(items)
        items.append('')
        items[-1] = items[0]
        items.remove(items[0])
        Rpermute(items, level-1)

if __name__ == '__main__':
    items = [1,2,3,4]
    print(Rpermute(items, len(items)))
    for i in permute(items, len(items)):
        print(i)

