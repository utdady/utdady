def shellSort(items):
    gap = len(items) // 3
    while gap > 0:
      for start in range(gap):
        insertionSort(items, start, gap)
      print("After increment of size", gap, "the list is", items)
      gap //= 3

def insertionSort(items, start, gap):
    for i in range(start + gap, len(items), gap):
        m = items[i]
        while i >= gap and items[i - gap] > m:
            print(items[i], items[i - gap], items)
            items[i] = items[i - gap]
            i = i - gap
        items[i] = m

list_ = [54,26,93,17,77,31,44,55,20]
print(list_)
shellSort(list_)
print(list_)
