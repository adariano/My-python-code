tot = int(input())
jog = [x for x in map(int,input().split())]
sumb = sumc = 0
jog.sort(reverse= True)
print(jog)
for n in range(len(jog)):
    if n <= 10:
        sumc += jog[n]
    else:
        sumb += jog[n]


print(f'{sumc - sumb} {sumc} {sumb}')