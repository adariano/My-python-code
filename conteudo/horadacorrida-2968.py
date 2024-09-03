import math

v,n = map(int,input().split())

for i in range(1,10):
    totp = v * n
    ans = int((totp/100)*(i*10))
    if i == 9:
        print(ans)
    else:
        print(ans, end=" ")