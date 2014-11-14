class Node:
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
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        """
        Print tree path in order
        """
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

# test binary tree
node = Node("Rinne")
node.insert("Webber")
node.insert("Fisher")
node.insert("Jones")
node.insert("Gausted")

node.print_tree()

pass