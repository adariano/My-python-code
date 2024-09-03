import math

n = int(input())

for _ in range(0,n):
    str = input()
    strLeft = ''
    strRight = ''
    midIndex = len(str) // 2 - 1
    # print(midIndex)

    strLeft += str[:midIndex:-1]
    strRight += str[midIndex::-1]
    print(strRight+strLeft)

