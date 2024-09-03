con = 1

while True:
    b = int(input())

    if b == 0:
        break

    else:
        n50 = b // 50
        b = b % 50

        n10 = b // 10
        b = b % 10

        n5 = b // 5
        b = b % 5

        n1 = b // 1
        b = b % 1

        print(f'Teste {con}\n{n50} {n10} {n5} {n1}\n')
        con += 1


    
