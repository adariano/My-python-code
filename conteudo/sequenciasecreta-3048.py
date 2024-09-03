n = int(input())
aux = 0
ans = 0
# input()

for i in range(0,n):
    if i == 0:
        x = int(input(f'\n'))
        aux = x
        # input()
    else:    
        x = int(input(f'\n'))
        if x != aux:
            ans += 1
        aux = x
        # input()

print(ans+1)
