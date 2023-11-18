

while True:
    h1,m1,h2,m2 = map(int,input().split())

    if m1 == 0 and m2 == 0 and h1 == 0 and h2 == 0:
        break
    else:
        if h1 >= h2:
            ht = h2 + (24 - h1)
            mt = (ht * 60) + (m2) + (60 - m1)
            print(mt - 60)
        else:
            ht = h2 - h1
            mt = (ht * 60) + (m2) + (60 - m1)
            print(mt - 60)
            