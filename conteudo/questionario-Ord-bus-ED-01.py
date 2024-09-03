count = int(input())

for _ in range(count):
    plan = input()
    mat = [input() for x in range(3)]
    matstr = ''

    for k in range(3):
        matstr += str(mat[k])

    planlib = {}
    for i in range(len(plan)):
        if plan[i] not in planlib:
            planlib[plan[i]] = 1
        else:
            planlib[plan[i]] = planlib.get(plan[i]) + 1
    
    matstrlib = {}
    for i in range(len(matstr)):
        if matstr[i] not in matstrlib:
            matstrlib[matstr[i]] = 1
        else:
            matstrlib[matstr[i]] = matstrlib.get(matstr[i]) + 1
    
    if list(matstrlib.keys()) not in list(planlib.keys()):
        print('You Died!')
    elif len(matstrlib.keys()) < len(planlib.keys()):
        ans = ''
        for k in planlib.keys():
            if k not in matstrlib.keys():
                ans += ''.join([k for x in range(planlib.get(k))])
            elif matstrlib.get(k) < planlib.get(k):
                ans.join('{k}' for x in range(matstrlib.get(k) - planlib.get(k)))
        print(f'Bora ralar: {ans}')
    else:
        print("It's in the box!")

        

    # print(mat,matstr, plan, planlib, matstrlib)
