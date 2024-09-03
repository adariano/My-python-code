class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

class Fila_comPilhas:

    def __init__(self):
        self.pilha1 = Stack()
        self.pilha2 = Stack()

    def enqueue (self, item):
        self.pilha1.push(item)

    def dequeue (self):
        while self.pilha1.isEmpty() == False:
            self.pilha2.push(self.pilha1.pop())
        
        ans = self.pilha2.pop()

        while self.pilha2.isEmpty() == False:
            self.pilha1.push(self.pilha2.pop())
        
        return ans

    def imprime (self):
        while self.pilha1.isEmpty() == False:
            self.pilha2.push(self.pilha1.pop())
        
        while self.pilha2.isEmpty() == False:
            ans = self.pilha2.pop()
            print(ans)
            self.pilha1.push(ans)


fila = Fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
fila.imprime()

# fila = Fila_comPilhas()

# fila.enqueue(1)
# fila.enqueue(2)
# fila.enqueue(3)
# fila.enqueue(4)
# fila.enqueue(5)
# print('dequeue - '+str(fila.dequeue()))
# fila.enqueue(6)
# print('dequeue - '+str(fila.dequeue()))
# print('dequeue - '+str(fila.dequeue()))
# fila.imprime()