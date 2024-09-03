def divisores (num):
    list = []
    for i in range(num):
        if num % (i+1) == 0:
            list.append(i+1)
    return list
