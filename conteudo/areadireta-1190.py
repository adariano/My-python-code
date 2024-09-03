op = input()
ans = 0
div = 0
n = [[float(input()) for x in range(0,12)]for y in range(0,12)]

cont = 0
for i in range(1,6):    
    for j in range(11,10-cont,-1):
        ans+=n[i][j]
        div+=1

    cont+=1

cont = 0
for i in range(6,11):    
    for j in range(7+cont,12):
        ans+=n[i][j]
        div+=1

    cont+=1

if op == 'S':
    print(f'{ans:.1f}')
if op == 'M':
    print(f'{ans/div:.1f}')