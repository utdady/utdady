class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def is_palindrome(s):
    string = s
    p = Queue()
    q = Queue()
    for char in s:
        q.enqueue(char)

    for char in s[::-1]:
        p.enqueue(char)

    while (p.size() and q.size()) > 1:
        first = p.dequeue()
        last = q.dequeue()
        if first != last:
            return False
    return True

if __name__ == '__main__':
    data = 'madam'
    print(is_palindrome(data))
