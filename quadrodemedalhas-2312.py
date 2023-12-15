N = int(input())
qua ={}
        
for i in range(N):
    nome,o,p,b = input().split()
    o = int(o)
    p = int(p)
    b = int(b)
    qua[i] = [nome,o,p,b]

qua = dict(sorted(qua.items(), key= lambda x: (0-x[1][1],0-x[1][2],0-x[1][3],x[1][0])))

for i in qua.keys():
    print(*qua[i])