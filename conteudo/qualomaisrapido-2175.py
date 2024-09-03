def maisrpd (a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


o,b,i = map(float,input().split())

l = maisrpd(o,b,i)
#print(l)

if ((o == b) and b <= i) or ((o == i) and o <= b) or ((i == b) and b <= i):
    print("Empate")
elif l == o:
    print("Otavio")
elif l == b:
    print("Bruno")
elif l == i:
    print("Ian")