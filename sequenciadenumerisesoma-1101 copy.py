while True:
    m,n = map(int,input().split())

    if m > 0 and n > 0:
        if m < n:
            aux = m
            m = n
            n = aux
        sum = 0

        for i in range(n,m+1):
            print(i, end=' ')
            sum += i
        print(f'Sum={sum}')
            

    else:
        break