class PQueue:
    def __init__(self):
        self.values = [] 

    def __str__(self):
        return str(self.values)

    def empty(self):
        return len(self.values) == 0

    def enqueue(self, value):
        self.values.append(value)
        if self.values[len(self.values)] < self.values[len(self.values)-1]:
            temp = self.values[len(self.values)]
            self.values[len(self.values)] = self.value[len(self.values)-1]
            self.values[len(self.values)-1] = temp
        
    def dequeue(self):
        maxi = max(self.values)
        self.values.pop()
        return value
    
if __name__ == '__main__':
    pq = PQueue()
    data = [1, 3, 5, 2, 0, 6, 4]
    for i in data:
        pq.enqueue(i)
        print(pq)
      
    while not pq.empty():
        pq.dequeue()
        print(pq)
