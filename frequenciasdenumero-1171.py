n = int(input())
freq = []
dic = {}
for i in range(n):
    key = int(input())
    keytuple = lambda x:(x,0)
    freq.append(keytuple(key))

for ele in freq:
    aux = lambda x:x[0]
    if aux(ele) not in dic:
        dic[aux(ele)] = 1
    else:
        dic[aux(ele)] += 1

for ele in sorted(dic):
    print(f'{ele} aparece {dic[ele]} vez(es)')

