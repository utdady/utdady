class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s
    
class BST(BinaryTree):
    def search(tree, item):
        if tree is None or tree.key == item:
            return tree

        if tree.key < item:
            return BST.search(tree.rightChild, item)

        return BST.search(tree.leftChild, item)
        
    def is_found(tree, item):
        while tree.leftChild is not None and tree.rightChild is not None:
            if tree.leftChild.key == item:
                return True
            else:
                return BST.is_found(tree.leftChild, item)
            if tree.rightChild.key == item:
                return True
            else:
                return BST.is_found(tree.rightChild, item)

if __name__ == '__main__':
    r = BST(4)
    r.insertLeft(2)
    r.insertRight(6)
    r.getLeftChild().insertLeft(1)
    r.getLeftChild().insertRight(3)
    r.getRightChild().insertLeft(5)
    print(r)

    print(BST.search(r,5))
    assert BST.search(r,5) == '4 6 5'
    
    print(BST.search(r,3))
    assert BST.search(r,3) == '4 2 3'
    
    print(BST.search(r,7))
    assert BST.search(r,7) == '4 6'
    
    print(BST.is_found(r,5))
    assert BST.is_found(r,5) == True
    
    print(BST.is_found(r,3))
    assert BST.is_found(r,3) == True
    
    print(BST.is_found(r,7))
    assert BST.is_found(r,7) == False
