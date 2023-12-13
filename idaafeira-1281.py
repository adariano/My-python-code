n = int(input())

for _ in range(n):
    card = {}
    lista = {}
    m = int(input())
    
    for i in range(m):
        pro,pre = input().split()
        pre = float(pre)
        card[pro] = pre
    
    p = int(input())
    for i in range(p):
        pro,qtd = input().split()
        qtd = int(qtd)
        lista[pro] = qtd
    
    fund = 0
    for key in lista:
        fund += card[key] * lista[key]
    
    print(f'R$ {fund:.2f}')