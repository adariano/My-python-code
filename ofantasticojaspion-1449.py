t = int(input())

for _ in range(t):
    pal,mus = map(int,input().split())
    dic = {}

    for _ in range(pal):
        jap = input()
        port = input()
        dic[jap] = port
    
    musica = []
    for _ in range(mus):
        musica.append(input())

    for i in range(len(musica)):
        ans = ''
        for wor in musica[i].split():
            if wor in dic:
                ans += dic[wor]+' '
            else:
                ans += wor+' '
        print(ans[:-1])
    print()
