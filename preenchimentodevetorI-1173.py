n = []
n.append(int(input()))

for i in range(1,10):
    aux = n[i-1]*2
    n.append(aux)

for i in range(0,10):
    print(f'N[{i}] = {n[i]}')