class Tree:
    def __init__(self, value='', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        s = str(self.value)+ ':'
        if self != None:
            s += ' ' + str(self.left)
            s += ' ' + str(self.right)
        return s

# generate a tree from a list of items (data)            
def build_tree(data, index):
    t = None
    if index < len(data):
        left = build_tree(data, index*2+1)
        right = build_tree(data, index*2+2)
        t = Tree(data[index], left, right)
    return t

# recursively traverse through all nodes in a tree and return the maximum value
def find_max(tree, maximum):
    # your code goes here
    if tree == None:
        return maximum
    maximum = tree.value
    lmax = find_max(tree.left, maximum)
    rmax = find_max(tree.right, maximum)
    if lmax > maximum:
        maximum = lmax
    if rmax > maximum:
        maximum = rmax
    return maximum

if __name__ == '__main__':
    data = [1,2,10,7,4,8,6,5]
    t = build_tree(data, 0)
    # find the maximum number, initially it is set to -inf
    m = find_max(t,float('-inf'))
    print(m)
