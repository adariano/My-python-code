n  = int(input())

for _ in range(0,n):
    m = int(input())
    tot = 0
    fib = [0,1]
    # print(fib)

    if m > 1:
        for i in range(2,m+1):
            fib.append(fib[i-1]+fib[i-2])
    
    print(f'Fib({m}) = {fib[m]}')
