tam, n = [int(x) for x in input().split()]
if n == 0:
    items = []
else:
    items = [int(x) for x in input().split()]


tab = dict(zip(range(tam),[[] for _ in range(tam)]))
for num in items:
    tab[num % tam].append(num)

for item in tab.keys():
    if tab[item] == []:
        print(f'{item} - [x]')

    elif len(tab[item]) > 1:
        ans = f'{item} - '
        for i in tab[item]:
            ans += f'{i} -> '
        print(ans[:-4])
    else:
        ans = f'{item} - '
        ans += f'{tab[item]}'[1:-1]
        print(ans)

