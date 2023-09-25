def binarySearch(alist, item):
    first, last = 0, len(alist)-1
    index, found = -1, False
    while first <= last:
        midpoint = (first + last)//2
        if alist[ midpoint] == item:
            found = True
            index = midpoint
            break
        else:
            if item < alist[ midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1    
    return index 
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 1))
print(binarySearch(testlist, 17))
print(binarySearch(testlist, 0))
