np = 0
ni = 0
pos = 0
neg = 0

for i in range(0,5):
    a = int(input())

    if a % 2 == 0:
        np += 1
    else:
        ni += 1
    if a != 0:
        if a > 0:
            pos += 1
        else:
            neg += 1

#ans = ans / m

print(f'{np} valor(es) par(es)\n{ni} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)')
