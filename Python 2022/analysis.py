from timeit import Timer, timeit
from random import choice

def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items

def selectionSort(items):
   for i in range(len(items)-1,0,-1):
       m=0
       for j in range(1,i+1):          # find the maximum in the range
           if items[ j] > items[ m]:
               m = j                      
       items[ m], items[ i] = items[ i], items[ m]

def insertionSort(items):
   for i in range(1,len(items)):
     m = items[ i]
     while i > 0 and items[ i-1] > m:
         items[ i] = items[ i-1]
         i -= 1
     items[ i] = m

def shellSort(items):
    gap = len(items)//3
    while gap > 0:
      for start in range(gap):
        shellinsertionSort(items,start,gap)
      # print("After increment of size",gap,"the list is",items)
      gap //= 3

def shellinsertionSort(items,start,gap):
    for i in range(start+gap,len(items),gap):
        m = items[ i]
        while i >= gap and items[ i-gap] > m:
            items[ i] = items[ i-gap]
            i = i - gap
        items[ i] = m

def quickSort(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[ first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[ leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[ rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           alist[ leftmark], alist[ rightmark] = alist[ rightmark],alist[ leftmark]       
   alist[ first], alist[ rightmark] = alist[ rightmark], alist[ first]
   return rightmark

def mergeSort(items):
    # print("Splitting ",items)
    if len(items)>1:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        # print("Merging ",items)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[ i] <= r[ j]:
                items[ k] = l[ i]
                i += 1
            else:
                items[ k] = r[ j]
                j += 1
            k += 1
        while i < len(l):
            items[ k] = l[ i]
            i, k = i+1, k+1
        while j < len(r):
            items[ k] = r[ j]
            j, k = j+1, k+1

def countSort(arr, m):
    # count the same digits and put their counts at index = digit
    counts = [0 for i in range(m+2)] 
    for i in arr:
        counts[ i] += 1
    # convert counts into ranking: each index value = (number of items <= i) 
    for i in range(m+1):
        counts[ i] += counts[ i-1]

    output = [0 for i in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr)-1, -1, -1):
        # print(i,arr[ i],counts[arr[ i]])
        output[counts[arr[ i]]-1] = arr[ i]
        counts[arr[ i]] -= 1

    return output

def count_sort(arr, pos, m):
    # count the same digits and put their counts at index = digit
    counts = [0 for i in range(11)] 
    for i in arr:
        i = str(i)
        while len(i) < m: # add 0s in front to small numbers
            i = '0' + i 
        i = int(i[ pos])
        counts[ i] += 1
    # convert counts into ranking: each index value = (number of items <= i) 
    for i in range(10):
        counts[ i] += counts[ i-1]

    output = [0 for i in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr)-1, -1, -1):
        j = str(arr[ i])
        while len(j) < m:
            j = '0' + j
        j = int(j[ pos])
        output[counts[ j]-1] = arr[ i]
        counts[ j] -= 1

    return output

def radix_sort(arr, pos):
    for i in range(pos-1, -1, -1):
        arr = count_sort(arr,i,pos)
    return arr

def insertion_Sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b

list_ = list(range(0,500))      # list of numbers
d1 = [choice(list_) for i in range(5)]   # list of size 5
d2 = [choice(list_) for i in range(10)]  # list of size 10
d3 = [choice(list_) for i in range(20)]
d4 = [choice(list_) for i in range(40)]
d5 = [choice(list_) for i in range(80)]
d6 = [choice(list_) for i in range(160)]
d7 = [choice(list_) for i in range(320)]
d8 = [choice(list_) for i in range(500)]

# you need to add more lists of different sizes
data = [d1, d2, d3, d4, d5, d6, d7, d8]

for i in data:
    print('------------------------------------------------')
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    print("bubblSort |",t1.timeit(number=1), "milliseconds")

    t2 = Timer(f"selectionSort({i})", "from __main__ import selectionSort")
    print("selecSort |",t2.timeit(number=1), "milliseconds")

    t3 = Timer(f"insertionSort({i})", "from __main__ import insertionSort")
    print("inserSort |",t3.timeit(number=1), "milliseconds")

    t4 = Timer(f"shellSort({i})", "from __main__ import shellSort")
    print("shellSort |",t4.timeit(number=1), "milliseconds")

    t5 = Timer(f"quickSort({i}, {0}, {len(i)-1})", "from __main__ import quickSort")
    print("quickSort |",t5.timeit(number=1), "milliseconds")

    t6 = Timer(f"mergeSort({i})", "from __main__ import mergeSort")
    print("mergeSort |",t6.timeit(number=1), "milliseconds")

    t7 = Timer(f"countSort({i}, {max(i)})", "from __main__ import countSort")
    print("countSort |",t7.timeit(number=1), "milliseconds")

    t8 = Timer(f"radix_sort({i}, {len(str(max(i)))})", "from __main__ import radix_sort")
    print("radixSort |",t8.timeit(number=1), "milliseconds")
