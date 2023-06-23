class Stack:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        if len(self.array) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        self.array.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.array.pop()
        else:
            return 'Empty'

    def peek(self):
        return self.array[-1]
    
    def size(self):
        return len(self.array)

    '''
    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, char):
        try:
            a = self.precedence[char]
            b = self.precedence[self.peek()]
            if a <= b:
                return True
            else:
                return False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while ((not self.isEmpty()) and self.peek != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    if i == '^' and self.array[-1] == i:
                        break
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        print(''.join(self.output))
        '''
