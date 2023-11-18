n = int(input())

for n in range(1,n+1):
    a = n
    b = a ** 2
    c = a * b
    print(f'{a} {b} {c}')

    b += 1
    c += 1
    print(f'{a} {b} {c}')
