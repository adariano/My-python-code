class grafo:
    def __init__(self):
        self.vertList = {}
        self.numVert = 0
    
    def addVert(self,key):
        self.numVert += 1
        aux = vert(key)
        self.vertList[key] = aux
    
    def getVert(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    def getVerts(self):
        return self.vertList.keys()

    def addEdge(self,ini,fin):
        if ini not in self.vertList:
            self.addVert(ini)
        if fin not in self.vertList:
            self.addVert(fin)
        self.vertList[ini].addVizinho(fin)
    
    def getEdges(self,key):
        return self.vertList[key].getVizinhos()
    
    def __repr__(self):
        ans = ''
        for vert in self.vertList:
            ans += str(vert) + ':' + f'{self.vertList[vert].getVizinhos()}' + '\n'
        return ans[:-1]

    def delVert(self,key):
        if key in self.vertList:
            self.vertList.pop(key)
            for term in self.vertList:
                if key in self.vertList[term].getVizinhos():
                    self.vertList[term].delVizinho(key)
    
    def delEdge(self,ini,fin):
        if self.vertList[ini]:
            if self.vertList[fin]:
                self.vertList[ini].delVizinho(fin)


class vert:
        def __init__(self,key):
            self.chave = key
            self.vizinhos = []  
        
        def addVizinho(self,key):
            self.vizinhos.append(key)

        def delVizinho(self,key):
            self.vizinhos.remove(key)
        
        def getVizinhos(self):
            return self.vizinhos
        
        def getChave(self):
            return self.chave

G = grafo()
# G.addVert(1)
# G.addVert(2)
# G.addVert(3)
# G.addVert(4)
# G.addVert(5)

# G.addEdge(1,2)
# G.addEdge(2,1)
# G.addEdge(2,3)
# G.addEdge(4,1)
# G.addEdge(2,4)
# G.addEdge(2,5)
# G.addEdge(5,1)
# print(G,'\n')

# G.delVert(1)
# print(G,'\n')
# G.delEdge(2,4)
# print(G)

for n in range(int(input())):
    comand = input().split()
    if 'IV' in comand:
        G.addVert(comand[1])
    elif 'IA' in comand:
        G.addEdge(comand[1],comand[2])
    elif 'RV' in comand:
        G.delVert(comand[1])
    elif 'RA' in comand:
        G.delEdge(comand[1],comand[2])
    # print(G,'\n ------------')

# print(G)
ans = 0
for i in G.getVerts():
    aux = len(G.getVert(i).getVizinhos())
    if aux > ans: ans = aux

print(ans)