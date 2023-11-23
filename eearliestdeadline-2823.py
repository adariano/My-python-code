n = int(input())
cp = 0
pp = 0
totc = 0

for i in range(0,n):
    c,p = map(int,input().split())
    totc += c
    if i == 0:
        cp = p
        pp = p
    else:
        if pp != p:
            print('FAIL')
            break

if totc <= p:
    print('OK')
        