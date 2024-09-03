while True:
    n,j = map(int,input().split())

    if n == 0  and j == 0:
        break
    else:
        f = [input().split() for x in range(j)]
        check = [0 for _ in range(n)]

        for i in range(j):
            for k in range(max(len(x) for x in f)):
                f[i][k] = int(f[i][k])

                if f[i][k] == 1:
                    check[k] += 1
    
    flag = False
    for ele in check:
        if ele == j:
            print('yes')
            flag = True
            break
        
    if flag == False:
        print('no')