import math

while True:
    n = int(input())

    if n == 0:
        break
    else:
        cont = 0
        f=[]
        for i in range(n):

            f.append([1]*n)

        while cont < math.ceil(n/2):
            for i in range(cont,n-cont):
                for j in range(cont,n-cont):
                    f[i][j] = cont+1
            cont += 1


        for lista in f:
            for elemento in lista:
                print(f'  {elemento}', sep='  ', end='')
            print()
        print()
