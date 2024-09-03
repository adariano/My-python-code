class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        str = '{'

        for item in self.items:
            str += f'{item} '
        
        return str

class Deque:
    def __init__(self):
        self.items = []

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

    def size(self):
        return len(self.items)
    
    def moveEndIndex(self,item_index):
        self.addRear(int(self.items.pop(item_index)))

    def __str__(self):
        str = ''

        for item in self.items:
            str += f'{item}'

        return str

class comando():
    def __init__(self,prio,com,content,key):
        self.prio = int(prio)
        self.comando = com
        self.content = content
        self.key = key
    
    def __repr__(self):
        str = ''
        str += f'{self.prio}'
        str += f' {self.comando}'
        str += f' {self.content}'
        str += f' {self.key}'
        
        return str

class fila_prio():
    def __init__(self):
        self.lista = [Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]

    def enfileirar(self,item):
        self.lista[item.prio].enqueue(item)

    def proximo(self):
        for prio in self.lista:
            if prio.size() > 0:
                return prio.dequeue()
                break
    
    def __repr__(self):
        str = ''
        
        for fila in self.lista:
            if fila.size() > 0:
                str += f'{fila}, '
        return str
    # parte de enfileirar esta otima

fil = fila_prio()

while True:
    key = input()

    if 'enqueue' in key:
        for _ in range(int(key[8])):
            aux = input()

            if 'dekey' in aux:
                content_deque = Deque()
                content_lista = [int(x) for x in aux[8:].split()]
                content_key = int(content_lista[0])

                for n in range(1,len(content_lista)):
                    content_deque.addFront(content_lista[n])

                item = comando(aux[0],aux[2:7],content_deque,content_key)
                fil.enfileirar(item)
                # print(item)
            else:
                item = comando(aux[0],aux[2:10],aux[11:].replace(" ",""),0)
                fil.enfileirar(item)
                # print(item)
        # print(fil)
    #processamento de enqueue

    elif 'go' in key:
        passo = fil.proximo()
        if passo == None:
            continue
         
        if passo.comando == 'dekey':
            for _ in range(passo.key):
                if int(passo.content.items[0]) > int(passo.content.items[1]): #A > B
                    # passo.content.moveEndIndex(1)
                    aux_a = int(passo.content.items.pop(0))
                    aux_b = int(passo.content.items.pop(0))

                    passo.content.addRear(aux_a)
                    passo.content.addFront(aux_b)

                    # print(passo.content)
                else: #A < B
                    aux_a = int(passo.content.items.pop(0))
                    aux_b = int(passo.content.items.pop(0))
                    
                    passo.content.addRear(aux_b)
                    passo.content.addFront(aux_a)

                    # print(passo.content)

            print(passo.content)
        # processamento do dekey

        else:
            ans = []
            aux = ''
            flag = 0
            for i in range(len(passo.content)):
                if passo.content[i] == '(':
                    if flag == 1:
                        ans.insert(0,aux)
                    elif flag == 2:
                        ans.append(aux)
                    elif flag == 0:
                        ans.append(aux)
                    aux = ''
                    flag = 1
                    continue
                elif passo.content[i] == ')':
                    if flag == 1:
                        ans.insert(0,aux)
                    elif flag == 2:
                        ans.append(aux)
                    elif flag == 0:
                        ans.append(aux)
                    aux = ''
                    flag = 2
                    continue
                
                aux += passo.content[i]
                
                if i == len(passo.content)-1:
                    if flag == 1:
                        ans.insert(0,aux)
                    elif flag == 2:
                        ans.append(aux)
                    elif flag == 0:
                        ans.append(aux)

            ans_final = ''
            for item in ans:
                if item != '':
                    ans_final += item
            print(ans_final)
        #processamento de scramble

    else:
        ans = 0
        for fila in fil.lista:
            ans += fila.size()
        
        print(f'{ans} processo(s) órfão(s).')
        break
