clas = {
    0: 0,
    1: 0,
    2: 0
}

for x in range(int(input())):
    obj = int(input())
    if obj < 10 and obj > clas.get(0):
        clas.update({0: obj})
    elif (obj >= 10 and obj < 20) and obj > clas.get(1):
        clas.update({1: obj})
    elif obj >= 20 and obj > clas.get(2):
        clas.update({2: obj})

print(*clas.values())