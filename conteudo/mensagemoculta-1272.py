n = int(input())

for _ in range(0,n):
    str = input()
    ans = ''
    flag = True

    for i in str:
        if i != ' ' and flag == True:
            ans += i
            flag = False
            continue
        elif i == ' ':
            flag = True
    
    print(ans)