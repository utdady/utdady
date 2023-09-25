def mergeSort(items):
    #print("Splitting ",items)
    if len(items) > 1:
        mid = len(items) // 2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        #print("Merging ",items)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                #print('left', items[k], l[i])
                items[k] = l[i]
                print('1',items)
                i += 1
            else:
                #print('right', items[k], r[j])
                items[k] = r[j]
                print('2',items)
                j += 1
            k += 1
        while i < len(l):
            #print('left', items[k], l[i])
            items[k] = l[i]
            print('3', items)
            i, k = i + 1, k + 1
        while j < len(r):
            #print('right', items[k], r[j])
            items[k] = r[j]
            print('4',items)
            j, k = j + 1, k + 1

list_ = [54,26,93,17,77,31,44,55,20]
mergeSort(list_)
print(list_)
