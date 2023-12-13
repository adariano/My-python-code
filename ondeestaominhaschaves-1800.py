q,e = map(int,input().split())
vis = {}

for esc in input().split():
    esc = int(esc)
    vis[esc] = True

for _ in range(q):
    esc = int(input())
    if esc not in vis:
        vis[esc] = True
        print('1')
    else:
        print('0')