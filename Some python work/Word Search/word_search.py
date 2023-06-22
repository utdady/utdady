import re
import sys

dictionary = []
f = open("/usr/share/dict/american-english", "r")
for line in f:
    word = re.sub("[\n|'|-]","",line)
    dictionary.append(word)
f.close()

def row_check(matrix, n):
    for word in matrix:
        if len(word) >= n:
            yield word

def col_check(matrix, length, n):
    word = ''
    j = 0
    while j < length:
        for i in range(length):
            word += matrix[i][j]
        if len(word) >= n:
            yield word
        word = ''
        j += 1

def ldiags_check(matrix, length, n):
    k, l = 1, 1
    word1, word2, word3 = '', '', ''
    for i in range(length):
        word1 += matrix[i][i]
        if i == 9:
            break
    if len(word1) >= n:
        yield word1
    while k < length:
        for i in range(length):
            if (i + k) < length:
                word2 += matrix[i][i + k]
        if len(word2) >= n:
            yield word2
        word2 = ''
        k += 1
    while l < length:
        for i in range(length):
            if (i + l) < length:
                word3 += matrix[i + l][i]
        if len(word3) >= n:
            yield word3
        word3 = ''
        l += 1

def rdiags_check(matrix, length, n):
    k = 0
    word = ''
    while k < (2 * length) - 1:
        for i in range(length):
            for j in range(length):
                if (i + j) == k:
                    word += matrix[i][j]
        if len(word) >= n:
            yield word
        word = ''
        k += 1

def words(a, b, c, d):
    w_ = []
    wl = set()
    for words in a:
        w_.append(words)
        rev = words[::-1]
        w_.append(rev)
    for words in b:
        w_.append(words)
        rev = words[::-1]
        w_.append(rev)
    for words in c:
        w_.append(words)
        rev = words[::-1]
        w_.append(rev)
    for words in d:
        w_.append(words)
        rev = words[::-1]
        w_.append(rev)
    for ele in w_:
        wl.add(ele)
    wordl = list(wl)
    return wordl

def word_check(word_list, n):
    wlist = []
    for w in word_list:
        for ws in dictionary:
            x = re.search(ws, w)
            if x and len(ws) >= n:
                wlist.append(ws)
    return wlist

def matrix_conv(io, N):
    n = int(N)
    grid = re.split("\n", io)
    length = len(grid)
    a = row_check(grid, n)
    b = col_check(grid, length, n)
    c = ldiags_check(grid, length, n)
    d = rdiags_check(grid, length, n)
    e = words(a, b, c, d)
    f = word_check(e, n)
    g = sorted(f)
    return g

def main():
    x = sys.stdin.read()
    y = sys.stdin.read()
    z = matrix_conv(x, y)
    print(z)
    
main()

