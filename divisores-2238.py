a,b,c,d = map(int,input().split())
aux = 0

while True:
    aux += a
    if aux < c:
        if aux % b != 0:
            if d % aux != 0:
                print(aux)
                break
    else:
        print('-1')
        break
