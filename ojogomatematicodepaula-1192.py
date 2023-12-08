def resultado(f):
    n1 = int(f[0])
    n2 = int(f[2])
    dig = f[1]

    if n1 == n2:
        return n1*n2
    elif ord(dig) > 64 and ord(dig) < 91:
        return n2 - n1
    else:
        return n1 + n2


n = int(input())

for _ in range(0,n):
    comb = input()
    print(resultado(comb))