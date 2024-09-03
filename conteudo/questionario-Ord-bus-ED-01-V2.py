class estudo:

    def __init__(self, nome):
        self.nome = nome
        self.bib = {}
    
    def create_lib(self):
        list = [x for x in self.nome]
        for let in list:
            if let not in self.bib:
                self.bib[let] = 1
            else:
                self.bib[let] += 1
        return self.bib
    
    def add_lib(self,word):
        list = [x for x in word]
        for let in list:
            if let not in self.bib:
                self.bib[let] = 1
            else:
                self.bib[let] += 1
        return self.bib


for _ in range(int(input())):
    plan = estudo(input())
    plan.create_lib()
    
    mat = estudo(input())
    mat.create_lib()
    for _ in range(2):
        mat.add_lib(input())
# 
    # flag = False
    for let in mat.bib.keys():
        if let in plan.bib.keys():
            mat.bib[let] -= plan.bib[let]
        else:
            print('You died!')
            # flag = True
            break
    # if flag == True:
        # break

    if all(list(map(lambda x: 1 if x == 0 else 0, mat.bib.values()))) == True and len(mat.bib.keys()) == len(plan.bib.keys()):
        print("It's in the box!")
    
    ans = ''
    for let in plan.bib.keys():     
        if let not in mat.bib.keys():
            ans += f'{let}'*(plan.bib[let])

    if ans != '': 
        print(f'Bora ralar: {ans}')


    # print(plan.bib,mat.bib)

    # if len(plan.bib.keys()) < len(mat.bib.keys()):
    #     print('You died!')
    #     break
    # else:
    #     for i in mat.bib.keys():
    #         for j in plan.bib.keys():
    #             if i in plan.bib.keys():
    #                 if mat[i] == plan[j]:
                        



