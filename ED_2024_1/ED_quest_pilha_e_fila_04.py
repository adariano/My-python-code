class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty == False:
            return self.items.pop()

    def peek(self):
        if self.isEmpty == False:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.pop()
s.push(3)
while not s.isEmpty():
    print(s.pop())