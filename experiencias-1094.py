n = int(input())
tot = 0
totc = 0
totr = 0
tots = 0

for i in range(0,n):
        qtd,typ = map(str,input().split())
        qtd = int(qtd)

        tot += qtd

        if typ == 'C':
            totc += qtd
        elif typ == 'R':
            totr += qtd
        elif typ == 'S':
            tots += qtd

print(f'Total: {tot} cobaias\nTotal de coelhos: {totc}\nTotal de ratos: {totr}\nTotal de sapos: {tots}')
print(f'Percentual de coelhos: {(totc/tot) * 100:.2f} %\nPercentual de ratos: {(totr/tot) * 100:.2f} %\nPercentual de sapos: {(tots/tot) * 100:.2f} %')
        