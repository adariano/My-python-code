class arvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.tam = 0
    
    def tamanho(self):
        return self.tam
    
    def put(self,key):
        #check para existencia da raiz mestre, se sim,
        if self.raiz:
            #mande o node atual, com uma key para ser adicionada
            self._put(key,self.raiz)
        #se não, crie um root com o valor
        else:
            self.raiz = arvoreNode(key)
        
        self.tam += 1

    def _put(self,key,nodeAtual):
        #se menor, vai pra esquerda
        if key < nodeAtual.key:
            #se ja estiver ocupado
            if nodeAtual.filhoEsqCheck():
                #manda o filho esquerdo dele recursivamente
                self._put(key,nodeAtual.filhoEsq)
            #se não estiver ocupado, crie um node novo com a key e pai o node atual com filho esq vazio
            else:
                nodeAtual.filhoEsq = arvoreNode(key,pai=nodeAtual)
        #se maior, vai pra direita
        else:
            if nodeAtual.filhoDirCheck():
                self._put(key,nodeAtual.filhoDir)
            else:
                nodeAtual.filhoDir = arvoreNode(key,pai=nodeAtual)
    
    def largura(self,larg=0):
        #se existir uma raiz mestre, mande ela para _largura
        if self.raiz:
            return self._largura(self.raiz,larg) 
        else:
            return larg
    
    def _largura(self,nodeAtual,larg,aux=0):
        #se primeiro, ela tiver um filho na esquerda 
        if nodeAtual.filhoEsqCheck():
            aux = self._largura(nodeAtual.filhoEsq,larg+1,aux)
        if nodeAtual.filhoDirCheck():
           aux = self._largura(nodeAtual.filhoDir,larg+1,aux)                
        if aux < larg: aux = larg
        return aux
        #a coisa mais bonita que ja fiz ;-;

class arvoreNode:
    def __init__(self,key,esq=None,Dir=None,pai=None):
        self.key = key
        self.filhoEsq = esq
        self.filhoDir = Dir
        self.pai = pai

    def filhoEsqCheck(self):
        return self.filhoEsq
    
    def filhoDirCheck(self):
        return self.filhoDir
    
    def raizCheck(self):
        return not self.pai
    
    def raizCheck(self):
        return not (self.filhoDir or self.filhoEsq)
    
n = int(input())
lista = [int(x) for x in input().split()]
A = arvoreBinariaBusca()
for item in lista: A.put(item)
print(A.largura())