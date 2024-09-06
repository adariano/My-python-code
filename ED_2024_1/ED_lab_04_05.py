class perf:
    def __init__(self,nome):
        self.nome = nome
        self.amigos = []
    
    def addAmigo(self,nome):
        self.amigos.append(nome)
    
    def getAmigos(self):
        return self.amigos

    def __repr__(self):
        str = self.nome + ' -> '
        for item in self.amigos: str += item + ' '
        return str

class grafo:
    def __init__(self):
        self.socialDic = {}
    
    def addPerf(self,nome):
        aux = perf(nome)
        self.socialDic[nome] = aux
    
    def getPerfAmigos(self,nome):
        return self.socialDic[nome].getAmigos()

    def getPossibleAmigos(self,nome):
        jaAmigos = self.socialDic[nome].getAmigos()
        recomend = []

        for perfKey in self.socialDic:
            if perfKey == nome or perfKey in jaAmigos:
                continue
            else:
                # if jaAmigos in self.socialDic[perfKey].getAmigos():
                count = 0
                for elem in jaAmigos:
                    if elem in self.socialDic[perfKey].getAmigos():
                        count += 1
                    if count >= 3:
                        recomend.append(perfKey)
                        break
        if recomend == []:
            print('Cacildis! Cade elis?')
        else:
            for j in sorted(recomend): print(j)

S = grafo()

for n in range(int(input())):
    comand = input().split()
    S.addPerf(comand[0])
    for i in range(int(comand[1])):
        S.socialDic[comand[0]].addAmigo(comand[i+2])
    
    #print(S.socialDic[comand[0]])

S.getPossibleAmigos('Mussum')