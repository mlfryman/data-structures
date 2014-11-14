class Tree:
    """
    Tree node: left and right child + data, which can be any object
    """
    def __init__(self, data):
        """
        Tree node constructor
        @param: data node, data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        @param: data node, new data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def printTree(self):
        """
        Print tree path in order
        """
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

# test binary tree
tree = Tree("Rinne")
tree.insert("Webber")
tree.insert("Fisher")
tree.insert("Jones")
tree.insert("Gausted")

tree.printTree()

pass