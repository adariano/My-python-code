def printodd (x,y):
    #print(f'teste {y}')
    #print(f'teste {x}')
    if y < 6:
        y += 1
        
        if x % 2 == 0:
            x += 1
            print(x)
        
        else:
            if y == 1:
                print(x)
            else:
                x += 2
                print(x)
        
        printodd(x,y)
    

x = int(input())
printodd(x,0)
