### Chyld's solution ###
class Node:
    self.data = data
    self.prev = None
    self.next = None


class BinaryTree:
    root = None
    def to_list(self):
        list = []
        if self.root:
            self.visit_node(self.root, list)
        return list

    # recursive
    def visit_node(self, node, list):
        if node.prev:
            self.visit_node(node.prev, list)
        list.append(node.data)
        if node.next:
            self.visit_node(node.next, list)

    # find returns the parent of the new node
    def find(self, name, node = None):
        if not node:
            node = self.root
        if name < node.data and node.prev:
            return self.find(name, node.prev)
        elif name > node.data and node.next:
            return self.find(name, node.next)
        else:
            return node

    def insert(self, name):
        if not self.root:
            self.root = Node(name)
        else:
            node = self.find(name)
            if name < node.data:
                node.prev = Node(name)
            else:
                node.next = Node(name)


people = BinaryTree()
people.insert("Mark")
people.insert("Charlie")
people.insert("Alex")
people.insert("Donnie")
people.insert("Bob")
people.insert("Barnie")
people.insert("Peter")
people.insert("Sam")
people.insert("Rex")
people.insert("")

people.to_list()


### END Chyld's solution ###


### My solution ###
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
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

# test binary tree
tree = Tree("Trotz")
tree.insert("Webber")
tree.insert("Fisher")
tree.insert("Rinne")
tree.insert("Jones")
tree.insert("Gausted")

tree.print_tree()

pass