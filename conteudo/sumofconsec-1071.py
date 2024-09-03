def sumodd (a,b,sum):
    if a % 2 == 0:
        a -= 1
    else:
        a -= 2

    if a > b:
        sum += a
        sumodd(a,b,sum)
    return sum

x = int(input())
y = int(input())
ans = sumodd(x,y,0)

print(ans)