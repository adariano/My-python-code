n = int(input())
f = [int(x) for x in input().split()]
ans = 1

for i in range(0,n-2):
    if f[i] - f[i+1] != f[i+1] - f[i+2]:
        ans += 1

print(ans)