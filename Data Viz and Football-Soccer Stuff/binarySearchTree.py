from bNode import Node

class binSearchTree:
    def __init__(self):
        self.root = None

    def insertVal(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            child = self.root
            parent = None
            while child != None:
                parent = child
                if value <= child.data:
                    child = child.left
                else:
                    child = child.right
            if value <= parent.data:
                parent.left = Node(value)
            else:
                parent.right = Node(value)
        print('Value Inserted!!')

    def inorderTraversal(self):
        def inorder(root):
            if root != None:
                inorder(root.left)
                print(root.data, end= ' ')
                inorder(root.right)
        inorder(self.root)

    def preorderTraversal(self):
        def preorder(root):
            if root != None:
                print(root.data, end= ' ')
                preorder(root.left)
                preorder(root.right)
        preorder(self.root)

    def postorderTraversal(self):
        def postorder(root):
            if root != None:
                postorder(root.left)
                postorder(root.right)
                print(root.data, end= ' ')
        postorder(self.root)

    def treeHeight(self):
        def height(root):
            if root == None or (root.left == None and root.right == None):
                return 0
            else:
                return max(height(root.left), height(root.right)) + 1
        return height(self.root)

    def levelorderTraversal(self):
        result, current = [], [self.root]
        while current:
            nextLevel, vals = [], []
            for node in current:
                vals.append(node.data)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            current = nextLevel
            result.append(vals)
        return result
