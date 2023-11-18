def factorial (f,n):
    if n > 1:
        f = f * n
        factorial(f,n-1)
    else:
        print(f)


f = int(input())

factorial(f,f-1)