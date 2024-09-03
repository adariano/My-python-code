m,n = map(int,input().split())
dic = {}

for _ in range(m):
    nom,num = input().split()
    num = int(num)
    dic.update({nom: {'dinheiro': num, 'qtd': 0}})


str = ['']*n
for i in range(n):
    while True:
        strtemp = input()
        if strtemp == '.':
            break
        str[i] += strtemp+' '
        
for i in range(n):
    fund = 0
    for wor in str[i].split():
        if wor in dic.keys():
            fund += dic[wor]['dinheiro']
    print(fund)
