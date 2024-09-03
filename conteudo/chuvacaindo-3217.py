def menorpre (l,k,t1,t2,h):
    if h < l:
        return h
    else:
        h1 = 
        

def maiorpre (l,k,t1,t2,h):
    if h < l:
        return h
    else:
        if kg > k:
            return kg*t1
        else:
            return k

l,k,t1,t2,h = map(float,input().split())


print(f'{menorpre(l,k,t1,t2,h):.6f} {maiorpre(l,k,t1,t2,h):.6f}')
