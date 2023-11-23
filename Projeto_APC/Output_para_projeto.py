# t = input()

# for i in range(len(t)):
#     print(f'{i}{t[i]} ', end='')

# # os espaços " " dos inputs no beecrwod são aparentemente removidos nos exemplos inputs

r = 'portugal'

for i in range(len(r)):
    if ord(r[i]) in [97:123]:
        print(r[i])