n = int(input())

f = [[]for _ in range(n-1)]
f.insert(0, input().split())

for i in range(1,n):
    for j in range(len(f[i-1])-1):
        if f[i-1][j] == f[i-1][j+1]:
            f[i].append(1)
        else:
            f[i].append(-1)

if f[n-1][0] == 1:
    print('preta')
elif f[n-1][0] == -1:
    print('branca')