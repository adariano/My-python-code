a1,a2,a3,a4 = map(int,input().split())

if a2 > a1:
    aux = a1
    a1 = a2
    a2 = aux

if a3 > a2:
    aux = a2
    a2 = a3
    a3 = aux

if a4 > a3:
    aux = a3
    a3 = a4
    a4 = aux

#print(f'{a1} {a2} {a3} {a4}')

if a2 > a1:
    aux = a1
    a1 = a2
    a2 = aux

if a3 > a2:
    aux = a2
    a2 = a3
    a3 = aux

if a2 > a1:
    aux = a1
    a1 = a2
    a2 = aux

#print(f'{a1} {a2} {a3} {a4}')

if (a2 + a3 + a4) <= a1:
    print('S')
else:
    print('N')