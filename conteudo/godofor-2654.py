n = int(input())
f = [input().split() for _ in range(n)]
fans = []

def hiIndex(lista,ind):
    nova_lista = []
    lista.sort(key=lambda lista: lista[ind], reverse=True)
    nova_lista.append(lista[0])
    for i in range(1,len(lista)):
        if lista[i][ind] == nova_lista[0][ind]:
            nova_lista.append(lista[i])
    return nova_lista

for i in range(n):
    for j in range(1,4):
        f[i][j] = int(f[i][j])

for i in range(1,4):
    aux = []
    aux = hiIndex(f,i)
    f = []
    f = aux
    if len(f) == 1:
        break
    
if len(f) > 1:
    f.sort(key=lambda f:f[0])
    print(f[0][0])
else:
    print(f[0][0])

