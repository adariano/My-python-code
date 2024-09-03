# primeiro a altura > peso > sobrenome
class homi:
    def __init__(self,nome,sobrenome,altura,peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.altura = altura
        self.peso = peso
        self.dados = [nome, sobrenome, altura, peso]
    
    def add_List(self,nome,sobrenome,altura,peso):
        list = [nome, sobrenome, altura, peso]
        self.dados.append(list)
    
    

n = int(input())

lista = homi(map())
for _ in range(int(input())-1):
    lista.homi.add_List(input().split())

print(lista.homi)