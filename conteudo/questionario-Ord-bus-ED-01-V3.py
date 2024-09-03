class estudo:
    def __init__(self,nome):
        self.nome = nome
        self.list = [x for x in self.nome]
    
    def add_list(self,word):
        for n in range(len(word)):
            self.list.append(word[n])

for _ in range(int(input())):
    plan = estudo(input())
    mat = estudo(input())

    for n in range(2):
        mat.add_list(input())
    
    plan.list.sort()
    print(plan.list)
    mat.list.sort()
    print(mat.list)

    for i in range(len(plan.list)):
        if plan.list[i] in mat.list and :
