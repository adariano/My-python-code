n = int(input())

for i in range(0,n):
    m = int(input())
    xb,yb = map(int,input().split())
    anspos = 0
    ansdis = 3200

    for j in range(1,m+1):
        x1,y1 = map(int,input().split())

        dist = ((x1 - xb)**2 + (y1 - yb)**2)**0.5
        if dist < ansdis:
            ansdis = dist
            anspos = j

    
    print(anspos)

        
