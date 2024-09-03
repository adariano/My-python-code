class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

fila = Queue()
ans = ''

for char in input():
    if char in '*':
        ans += fila.dequeue()
    else:
        fila.enqueue(char)

print(ans)