x = []

for i in range(0,10):
    aux = int(input())
    if aux <= 0:
        aux = 1
        x.append(aux)
    else:
        x.append(aux)

for i in range(0,10):
    print(f'X[{i}] = {x[i]}')