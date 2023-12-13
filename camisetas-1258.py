            
while True:    
    N = int(input())
    if N == 0:
        break
    else:
        cam = {}

        for _ in range(N):
            nome = input()
            cor,tam = input().split()
            cam[nome] = {'cor': cor, 'tamanho': tam}
        
        ans = [[None,None,None]for x in range(N)]
        for nome,i in zip(cam,range(len(ans))):
            ans[i][2] = nome
            ans[i][1] = cam[nome]['tamanho']
            ans[i][0] = cam[nome]['cor']

        ans = sorted(ans, key= lambda x:x[0])
        ans = sorted(ans, key= lambda x:x[1],reverse=True)
        # ans = sorted(ans, key= lambda x:x[2])

        for ele in ans:
            print(f'{ele[0]} {ele[1]} {ele[2]}')

