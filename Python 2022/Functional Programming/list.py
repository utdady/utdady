'''
Prompt: Create a list comprehension that generates a list of items B from
        another list A where each item equals to a sum of two consecutive items
        in the original list: B[i] = A[i] + A[i+1]. For example, if the original
        list is [1, 3, 2, 4] then the list comprehension should have the
        following items: [4, 5, 6] where 4 = 1 + 3, 5 = 3 + 2, 6 = 2 + 4.
'''

# Function to modify list.
def listmodify(A):
    B = [x + y for x, y in zip(A, A[1:] + [A[0]])]
    return B[0: len(A) - 1]

# Main
def main():
    print(listmodify([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    main()
