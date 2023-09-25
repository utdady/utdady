def matrixI(matrix):
    length = len(matrix)
    det = determinant(matrix)
    adj = adjoint(matrix)
    for row in range(length):
        for col in range(length):
            adj[row][col] = float(adj[row][col] / det)
    return adj
    

def transposeMatrix(matrix):
    length = len(matrix)
    transpose = [[None for i in range(length)] for j in range(length)]
    for p in range(length):
        for q in range(length):
            transpose[p][q] = matrix[q][p]
    return transpose


def identityMatrix(length):
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


def determinant(matrix, total=0):
    length = len(matrix)
    indices = list(range(length))
     
    if length == 2 and len(matrix[0]) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det
 
    for col in indices:
        temp = copy_matrix(matrix)
        temp = temp[1:]
        height = len(temp) 
 
        for row in range(height):
            temp[row] = temp[row][0:col] + temp[row][col+1:] 
 
        sign = (-1) ** (col % 2)
        sub = determinant(temp)
        total += sign * matrix[0][col] * sub 
 
    return total

def adjoint(matrix):
    length = len(matrix)
    temp = [[None for i in range(length)] for j in range(length)]
    for row in range(length):
        for col in range(length):
            temp[row][col] = ((-1) ** (row + col)) * determinant(convmat(row, col, matrix))
    adjoint = transposeMatrix(temp)
    return adjoint

def copy_matrix(matrix):

    return matrix

def main():
    matrix = [[1,0,0],[0,1,0],[0,0,1]]
    result = matrixI(matrix)
    print(result)

main()
