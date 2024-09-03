tea = int(input())
a,b,c,d,e = map(int,input().split())

total = 0

if a == tea:
    total += 1
if b == tea:
    total += 1
if c == tea:
    total += 1
if d == tea:
    total += 1
if e == tea:
    total += 1

print(total)