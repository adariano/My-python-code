while True:
    n,b = map(int,input().split())
    if n == 0 and b == 0:
        break
    else:
        check = [False for i in range(n+1)]
        lista = input().split()
        for i in range(len(lista)): lista[i] = int(lista[i])
        # print(lista)

        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i] != lista[j]:
                    aux = lista[i] - lista[j]
                    if aux < 0:
                        aux = aux*-1

                    if aux in range(len(check)):
                        check[aux] = True

                    else:
                        continue
        check.remove(False)
        if False in check:
            print('N')
        else:
            print('Y')
