n = int(input())
cont = 0

for _ in range(0,n):
    diet = input()
    cafm = input()
    almo = input()
    tot = almo + cafm
    ans = ''
    flag = False
    
    for j in tot:
        if j not in diet:
            flag = True

    if flag == True:
        print('CHEATER')
        continue

    for i in diet:
        if i in tot:
            continue
        else:
            ans += i

    ans = sorted(ans)
    ans = ''.join(ans)
    print(ans)