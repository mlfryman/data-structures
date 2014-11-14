class Stack:
    data = []
     # self = food
    def push(self, name):
        # append(self, x) - self is implied, adds it for you
        self.data.append(name)
    def pop(self):
        self.data.pop()
