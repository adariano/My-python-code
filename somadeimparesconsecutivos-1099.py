n =int(input())

for i in range(0,n):
    x,y = map(int,input().split())
    ans = 0

    if x > y:
        aux = y
        y = x
        x = aux
    
    k = 0
    
    while x < y:
        if x % 2 == 0:
            x += 1
        elif x % 2 != 0 and k == 0:
            x += 2
        else:
            ans += x
            x += 2
        k += 1
    
    print(ans)



