while True:
    x,y = map(int,input().split())

    if x > 0 and y > 0:
        if x > y:
            aux = x
            x = y
            y = aux
        
        sum = 0
        for i in range(x,y+1):
            sum += i
        
        print(f'{x} {x+1} {x+2} {x+3} Sum={sum}')
    else:
        break