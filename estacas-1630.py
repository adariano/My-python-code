def mdc(a,b):
    if b == 0:
        return a
    return mdc(b,a%b)

while True:
    try:
        x,y = map(int,input().split())
            
        if x < y:
            aux = x
            x = y
            y = aux
        
        dis = mdc(x,y)
        tot = 2*(x/dis) + 2*(y/dis)

        print(int(tot))
    except EOFError:
        break