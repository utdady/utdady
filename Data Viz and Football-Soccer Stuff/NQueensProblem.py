def matrixI(matrix):
    length = len(matrix)
    inverse = [[None for i in range(length)] for j in range(length)]
    
def matrixT(matrix):
    length = len(matrix)
    transpose = [[None for i in range(length)] for j in range(length)]

    for p in range(length):
        for q in range(length):
            transpose[p][q] = matrix[q][p]

    return transpose

def matrixId(length):
    identity = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            if i == j:
                identity[i][j] = 1

    return identity

def convmat(i, j, matrix):
    matlen = len(matrix)
    templen = matlen - 1
    tlst = []
    temp = [[None for p in range(templen)] for q in range(templen)]

    for row in range(matlen):
        for col in range(matlen):
            if row == i:
                pass
            else:
                if col == j:
                    pass
                else:
                    tlst.append(matrix[row][col])
    count = 0

    for k in range(templen):
        for l in range(templen):
            temp[k][l] = tlst[count]
            count += 1

    return temp

def determinant(matrix):
    result = 0
    res = determin(matrix, result)

    return res

def determin(matrix, result):
    length = len(matrix)
    if length == 1:
        return matrix[0][0]
    if length == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    for i in range(length):
        for j in range(length):
            mat = convmat(i, j, matrix)
            result += (((-1) ** (i + j)) * matrix[i][j]) * determin(mat, result)
    return result

def main():
    
    print("N Queens Problem Solver")
    num = int(input("Enter the chess board dimension: "))


main()
