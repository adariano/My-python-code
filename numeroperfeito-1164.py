n = int(input())

for i in range(0,n):
    x = int(input())
    sum = 0
    aux = 1

    while aux < x:
        if x % aux == 0:
            sum += aux
        aux += 1
    
    if sum == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
