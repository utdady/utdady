from stack import Stack
        
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.leftChild = self.leftChild
            self.leftChild = tree
            
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.rightChild = self.rightChild
            self.rightChild = tree
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    
    def __str__(self):
        return self.key

class Node:
    def __init__(self, data):
        self.key = data
        self.leftChild = None
        self.rightChild = None

class ExpTree:
    def __init__(self, exp):
        self.exp = exp
        self.root = None
        self.make_tree(self.exp)

    def isOperator(self, char):
      optr = [" ", "-", "*", "/", "^"]
      if char in optr:
         return True
      return False
        
    def make_tree(self, exp):
        s = Stack()
        self.root = Node(exp[-1])
        s.push(self.root)

        for i in "".join(reversed(exp[:-1])):
         curr_node = s.peek()
         if not curr_node.rightChild:
            temp = Node(i)
            curr_node.rightChild = temp
            if self.isOperator(i):
               s.push(temp)
         else:
            temp = Node(i)
            curr_node.leftChild = temp
            s.pop()
            if self.isOperator(i):
               s.push(temp)

    def __str__(self):
        return self.root.key
    
    def preorder(self, head):
        print(head.key, end=' ')
        if head.leftChild:
            self.preorder(head.leftChild)
        if head.rightChild:
            self.preorder(head.rightChild)

    def postorder(self, head):
        if head.leftChild:
            self.postorder(head.leftChild)
        if head.rightChild:
            self.postorder(head.rightChild)
        print(head.key, end=' ')

    def postfixExp(self):
        self.postorder(self.root)
        print()
            
    def inorder(self, head):
        if head.leftChild:
            self.inorder(head.leftChild)
        print(head.key, end=' ')
        if head.rightChild:
            self.inorder(head.rightChild)

    def infixExp(self):
        self.inorder(self.root)
        print()

    def evaluate():
        pass
