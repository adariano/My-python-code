            
while True:    
    N = int(input())
    if N == 0:
        break
    else:
        dic = {}
        for _ in range(N):
            nome = input()
            cor,tam = input().split()
        
            if cor not in dic:
                dic[cor] = [[tam,nome]]
            else:
                dic[cor].append([tam,nome])

        for key in sorted(dic):
            for i in range(len(dic[key])):
                print(key, end=' ')
                print(*dic[key][i])