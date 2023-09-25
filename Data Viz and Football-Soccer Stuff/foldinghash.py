test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# simple hashing based on the modulo operation
index = [x % 9 for x in test] 

# folding hash function
k = 0
for item in test:
    s = 0
    item = str(item)
    for i in item:
        s += int(i)
    index[ k] = s % len(test)
    k += 1
print(index)
