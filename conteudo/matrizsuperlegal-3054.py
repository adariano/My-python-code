l,c = map(int,input().split())
mat = [[x for x in input().split()]for y in range(l)]
print(mat)

mat_dic = {}

col = 0
lin = 0
if l > c:
    for mat_q in range(1,l):
        # print(f'{lin_cont},{col_cont}')

else:
    for mat_q in range(1,c):
        col += 1
        if lin > 
