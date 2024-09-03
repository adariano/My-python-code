class deque:
    def __init__(self,lista):
        self.items = lista
    
    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    
    def moveEndFront(self):
        self.addFront(self.removeRear())

    def __str__(self):
        str = ''

        for item in self.items:
            str += f'{item}'

        return str

fila = deque(input().split())

for n in range(int(input())):
    fila.moveEndFront()

print(f'Pessoa da frente: {fila.items[0]}\nPessoa do fim: {fila.items[-1]}')
