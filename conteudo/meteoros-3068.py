cont = 0
while True:
    x1,y1,x2,y2 = map(int,input().split())
    cont += 1
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    else:
        n = int(input())
        ans = 0
        
        for i in range(0,n):
            x3,y3 = map(int,input().split())

            if x3 >= x1 and x3 <= x2 and y3 <= y1 and y3 >= y2:
                ans += 1
    print(f'Teste {cont}\n{ans}')
        