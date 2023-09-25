import math
num = int(input("Enter Number: "))
srt = int(math.log(num, 10))
arr = []
for i in range(srt, -1, -1):
    ele = int(num / pow(10, i))
    arr.append(ele)
    num -= ele * pow(10, i)
print(arr)
