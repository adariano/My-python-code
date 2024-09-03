def mmc(x,y):
    if x < y:
        aux = x
        x = y
        y = aux
    
    mai = x

    while True:
        if mai % x == 0  and mai % y == 0:
            return mai
        else:
            mai += 1
        

a,b,c,d = map(int,input().split())

if b != d:
    den = mmc(b,d)
    num = int(((den / b) * a) + ((den / d) * c))
else:
    den = b
    num = a + c

aux = 2
while aux <= den and aux <= num:
    if den % aux == 0 and num % aux == 0:
        den /= aux
        num /= aux
    else:
        aux += 1

num = int(num)
den = int(den)

print(f'{num} {den}')