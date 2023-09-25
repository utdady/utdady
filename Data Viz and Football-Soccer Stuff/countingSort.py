# counting sort for digits 0 - 9

def countSort(arr, m):
    # count the same digits and put their counts at index = digit
    counts = [0 for i in range(m + 2)] 
    for i in arr:
        counts[i] += 1
    # convert counts into ranking: each index value = (number of items <= i) 
    for i in range(m + 1):
        counts[i] += counts[i - 1]

    output = [0 for i in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr) - 1, -1, -1):
        print(i, arr[i], counts[arr[i]])
        output[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1

    return output, counts, arr

# Driver program to test above function
arr = [100,10,6,7,0,9,3,4,11]
m = max(arr)
ans, count, arr = countSort(arr, m)
print(f"Sorted array is {ans}")
print(len(count))
print(len(arr))
