op = input()
ans = 0
cont = 0
div = 0
n = [[float(input()) for x in range(0,12)]for y in range(0,12)]

for i in range(0,12):
    for j in range(1+cont,12):
        ans += n[i][j]
        div+=1
    cont+=1

if op == 'S':
    print(f'{ans:.1f}')
elif op == 'M':
    print(f'{ans/div:.1f}')