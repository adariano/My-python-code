x,y,z = map(int,input().split())

if (x+y-z) == 0 or (x-y-z) == 0 or (y+x-z) == 0 or (y-x-z) == 0 or (z+x-y) == 0 or (z-x-y) == 0 or (x-y) == 0 or (x-z) == 0 or (y-z) == 0:
    print("S")
else:
    print("N")