def primos_gemeos(count):
    primos = {}
    countaux = 1

    while count > 0:
        flag = False
        while flag == False:
            countaux += 1

            for x in range(countaux-1,1,-1):
                if countaux % x == 0:
                    break
                elif x == 2: #se o primeiro numero for primo
                    for y in range(countaux+1,1,-1):
                        if (countaux+2) % y == 0:
                            break
                        elif y == 2: #se o segundo numero tambem for primo
                            primos[countaux] = countaux+2
                            flag = True
                            break
        count -= 1
    return [(x,y) for x,y in primos.items()]