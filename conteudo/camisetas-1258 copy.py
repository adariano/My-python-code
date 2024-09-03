cont = 0            
while True:
    N = int(input())
    if N == 0:
        break
    else:
        if cont >= 1:
            print()

        cam = {}

        for i in range(N):
            nome = input()
            inp = input().split()
            inp.append(nome)
            cam[i] = inp
        
        cam = dict(sorted(cam.items(),key=lambda x:x[1][2]))
        cam = dict(sorted(cam.items(),key=lambda x:x[1][1], reverse=True))
        cam = dict(sorted(cam.items(),key=lambda x:x[1][0]))        

        for ele in cam:
            print(*cam[ele])

    cont+=1