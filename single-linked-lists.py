###  Chyld's Implementation  ###

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList1:
    head = None

    def insert(self, obj):
        # if there is no head, it points to nothing
        if(not self.head):
            self.head = Node(obj)
        else:
            self.last().next = Node(obj)

    def last(self, node = None):
        if(not node):
            node = self.head
        if(not node.next):
            return node
        else:
            return self.last(node.next)

people = SingleLinkedList()
people.insert('Bob Boberson')
people.insert('Sue')
people.insert('Frank')



# ####  Trial Solution - correct, but inefficient  ###
# class SingleLinkedList:
#     head = None
#     def insert(self, obj):
#         # creates a new node
#         node = Node()
#         node.data = obj
#         # check if list is empty; if it is, it assigns head to new node
#         if not self.head:
#             self.head = node
#         # otherwise, runs getLastNode function recursively until it finds the last node in the linkedList
#         else:
#             # set new nodes pointer to old head
#             lastNode = self.getLastNode(self.head)
#             lastNode.next = node
#     # loops until gets a node w/o next
#     def getLastNode(self, node):
#         # does node passed in have a 'next'?
#         if not node.next:
#             return node
#         # once find a node whose next=Nil, passes back up chain
#         else:
#             return getLastNode(node.next)



pass