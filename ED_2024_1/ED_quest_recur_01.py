class arvore:
    def __init__(self,raiz,esq=None,dir=None):
        self.raiz = raiz
        self.esq = esq
        self.dir = dir

    def inserir_filho_esq(self,raiz,esq=None,dir=None):
        if self.esq == None:
            self.esq = arvore(raiz,esq,dir)
        else:
            aux = arvore(raiz,self.esq)
            self.esq = aux
    
    def inserir_filho_dir(self,raiz,esq=None,dir=None):
        if self.dir == None:
            self.dir = arvore(raiz,esq,dir)
        else:
            aux = arvore(raiz,None,self.dir)
            self.dir = aux
    
    def getFilhoEsq(self):
        return self.esq
    
    def getFilhoDir(self):
        return self.dir
    
    def __repr__(self):
        return f"[{self.raiz},[{self.esq}],[{self.dir}]"
    
    def inserir_lista(self,lista):
        

ars = arvore(2)
print(ars)
ars.inserir_filho_dir(3)
print(ars)

