while True:
    n = int(input())
    if n == 0:
        break
    else:
        for _ in range(n):
            dic = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}
            resposta = [int(x) for x in input().split()]
            aux = 0
            for ele in dic.keys():
                dic[ele] = resposta[aux]
                aux+=1

            ansaux = ''
            aux = 0
            flag = False
            for ele in dic.keys():
                if dic[ele] <= 127:
                    ansaux += ele
                    aux+=1
                if aux > 1:
                    print('*')
                    flag = True
                    break
            if flag == False:
                if ansaux != '':
                    print(ansaux)
                else:
                    print('*')
