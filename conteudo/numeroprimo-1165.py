n = int(input())

for i in range(0,n):
    x = int(input())
    aux = 1

    while aux < x:
        if x % aux == 0 and aux != x and aux != 1:
            print(f'{x} nao eh primo ')
            break
        elif aux == (x - 1):
            print(f'{x} eh primo')
        aux += 1

