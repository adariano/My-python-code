def modulo (a):
    if a < 0:
        a *= -1
    return a

i = 0

while True:
    x1,y1,x2,y2 = map(int,input().split())

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    else:
        if (modulo(x1 - x2) == modulo(y1 - y2) and (x1 - x2) != 0 and (y1 - y2) != 0) or ((x1 - x2) != 0 and (y1 - y2) == 0) or ((x1 - x2) == 0 and (y1 - y2) != 0):
            print('1')
        elif modulo(x1 - x2) != modulo(y1 - y2):
            print('2')
        else:
            print('0')
