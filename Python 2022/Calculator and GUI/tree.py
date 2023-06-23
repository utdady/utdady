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

class ExpTree(BinaryTree):
    def __init__(self, exp):
        super().__init__(exp)
        self.make_tree(exp)
        
    def make_tree(self, exp):
        print('he')
        pf = exp.split()
        pStack = Stack()
        eTree = BinaryTree('')
        pStack.push(eTree)
        currentTree = eTree

        for i in pf:
            if i == '(':
                currentTree.insertLeft('')
                pStack.push(currentTree)
                currentTree = currentTree.getLeftChild()
            elif i in ['+', '-', '*', '/']:
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                pStack.push(currentTree)
                currentTree = currentTree.getRightChild()
            elif i == ')':
                currentTree = pStack.pop()
            elif i not in ['+', '-', '*', '/']:
                try:
                    currentTree.setRootVal(int(i))
                    parent = pStack.pop()
                    currentTree = parent
                except ValueError:
                    raise ValueError(f'token {i} is not a valid integer')
        print('rh')
        return eTree

    def __str__(self):
        pass
    
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
            
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        if self.rightChild:
            self.rightChild.inorder()
        print(self.key)

    def evaluate():
        pass
