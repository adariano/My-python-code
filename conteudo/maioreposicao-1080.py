ans = 0

for i in range(1,101):
    x = int(input())
    if x > ans:
        ans = x
        anspos = i

print(f"{ans}\n{anspos}")

    