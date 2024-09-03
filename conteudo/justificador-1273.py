aux = 0

while True:
    n = int(input())

    if n == 0:
        break
    else:
        cont = 0
        hiPos = 0
        ans = ''
        str = ['']*n

        if aux != 0:
            print()
        aux+=1

        for i in range(0,n):
            str[i] = input()

            if len(str[i]) > cont:
                cont = len(str[i])
                hiPos = i

        for i in range(0,n):
            ans = ''
            ans += str[i]
            
            while len(ans) < len(str[hiPos]):
                ans = ' ' + ans
        
            print(ans)
