while True:
    try:
        n = int(input())
        f = [input() for _ in range(n)]

        f.sort()

        for i in f: print(i)

    except EOFError:
        break