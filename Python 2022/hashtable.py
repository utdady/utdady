class Hashtable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.arr = []

    def Hash(self, key):
        hashsum = 0
        for char in key:
            hashsum += ord(char)
        return hashsum % self.capacity

    def add(self, key, value):
        hash_key = self.Hash(key)
        self.arr.append([hash_key, value])
        print(self.arr)

    def get(self, key):
        arr_index = self.Hash(key)
        for i in range(len(self.arr)):
            if self.arr[i][0] == arr_index:
                return self.arr[i][1]

    def remove(self, value):
        index = 0
        while index < len(self.arr):
            if self.arr[index][1] == value:
                del self.arr[index]
            index += 1

    def get_size(self):
        return len(self.arr)

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

h = Hashtable()
data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

for i in range(len(data)):
    h.add(data[i], i)
for key in data:
    print(h.get(key))
n = h.get_size()
for i in range(n):
    h.remove(i)
print(h.is_empty())
