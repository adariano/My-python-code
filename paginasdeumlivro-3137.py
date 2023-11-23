p = int(input())
d = 0

# while p > 99999:
#     p -= 1
#     d += 6
# while P

for i in range (1,p+1):
    if i <= 9:
        d += 1
        continue
    elif i <= 99:
        d += 2
        continue
    elif i <= 999:
        d += 3
        continue
    elif i <= 9999:
        d += 4
        continue
    elif i <= 99999:
        d += 5
        continue
    elif i <= 999999:
        d += 6
        continue

print(d)