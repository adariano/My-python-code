class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        # Vai colocar o node novo com o item no temp
        temp = Node(item)
        # vai colocar se colocar na posição do head e o colocando como
        #próximo.
        temp.setNext(self.head)
        #retornando o head para a posição original
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        #Se achar o item, quebra o loop e continua
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        #Se for o primeiro da lista execute o primeiro if
        if previous == None:
            self.head = current.getNext()
        else:
        #Aqui vc estaria mexendo com os proprios nodes de self.head
            previous.setNext(current.getNext())  

def removerSegundaOcorrencia(L, n):
    atual = L.head
    pre = None
    found = False
    done = False

    for i in range(L.size()):
        if atual.getData() == n and found == False:
            found = True
        elif atual.getData() == n and found == True and done == False:
            pre.setNext(atual.getNext())
            atual = pre
            done = True
            atual = atual.getNext()
            continue

        pre = atual
        atual = atual.getNext()
    
    return L

L = UnorderedList()
L.add(1)
L.add(2)
L.add(3)
L.add(2)
L.add(4)
L.add(2)
L.add(5)
L.add(2)
L.add(6)
L.add(2)
L.add(7)
L = removerSegundaOcorrencia(L, 2)
print(f'Lista: {L}')