t = input()
espbranco = ''
informal = ''
maius = ''
minus = ''
pont = ''
bandasp = False
bandnum = False

for i in range(len(t)):
    #ASPAS para interromper
    if ord(t[i]) == 34:
        if bandasp == False:
            bandasp = True
            continue
        elif bandasp == True:
            bandasp = False
            continue
    if bandasp == True:
        continue

    #FLAG para NUMERO interromper
    if bandnum == True:
        if ord(t[i]) > 47 and ord(t[i]) < 58:
            informal += f'{i} '
            continue
        else:
            bandnum = False

    # letra MINUSCULA
    if ord(t[i]) >= 97 and ord(t[i]) <= 122:

        # Na primeira pos
        if i == 0:
            minus += f'{i} '
        
        # A VERIFICAÇÃO DE MINUSCULA APÓS PONTO "." SERÁ FEITA EM PONTUAÇÃO

    
    # letra MAIUSCULA
    if ord(t[i]) >= 65 and ord(t[i]) <= 90 and i != 0:
        j = i - 1
        while True: #retornando até achar um diferente de espaço
            if ord(t[j]) == 32:
                j -= 1
            elif ord(t[j]) == 46: #até achar o ponto
                break
            else:
                maius += f'{i} '
                break

    # ESPAÇO
    if ord(t[i]) == 32:
        if ord(t[i-1]) == 32 or ord(t[i+1]) == 32:
            espbranco += f'{i} '
    
    # NUMEROS
    if ord(t[i]) in range(48,58):
        if ord(t[i-1]) in range(0,47) or ord(t[i-1]) in range(58,124): #elemento ANTERIOR NÃO é um número
            if (ord(t[i-1]) != 32 and ord(t[i-1]) != 44 and ord(t[i-1]) != 46): #elemento ANTERIOR não é " " ou "," ou "."
                informal += f'{i} '
                bandnum = True
                continue

        if i != len(t)-1:
             if (ord(t[i+1]) in range(0,47) or ord(t[i+1]) in range(58,124)): #elemento POSTERIOR NÃO é um número
                if ord(t[i+1]) != 32 and ord(t[i+1]) != 44 and ord(t[i+1]) != 46: #elemento POSTERIOR não é " " ou "," ou "." 
                    informal += f'{i} '
                    continue

    # if ord(t[i]) in range(48,58):  
    #     if ord(t[i-1]) in range(0,47) or ord(t[i-1]) in range(58,124): #elemento ANTERIOR NÃO é um número
    #         if (ord(t[i-1]) != 32 and ord(t[i-1]) != 44 and ord(t[i-1]) != 46): #elemento ANTERIOR não é " " ou "," ou "." 
    #             informal += f'{i} '
    #             continue
    #     if i != len(t)-1:
    #         if (ord(t[i+1]) in range(0,47) or ord(t[i+1]) in range(58,124)): #elemento POSTERIOR NÃO é um número
    #             if ord(t[i+1]) != 32 and ord(t[i+1]) != 44 and ord(t[i+1]) != 46: #elemento POSTERIOR não é " " ou "," ou "." 
    #                 informal += f'{i} '
    #                 continue

    #PONTUAÇÃO
    if (ord(t[i]) == 44 or ord(t[i]) == 46) and i != len(t)-1:
        if ord(t[i-1]) == 32 or (ord(t[i-1]) != 32 and ord(t[i+1]) != 32):
            pont += f'{i} '
        j = i + 1
        if ord(t[i]) == 46:
            while ord(t[j]) == 32:
                j += 1
                if ord(t[j]) not in range(65,91) and ord(t[j]) != 32:
                    minus += f'{j} '
                

if espbranco == '' and informal == '' and maius == '' and minus == '' and pont == '':
    print('SIM')
else:
    print('NAO')
    if espbranco != '':
        print(f'ESPACO BRANCO\n{espbranco[:-1]}')
    if informal != '':
        print(f'INFORMAL\n{informal[:-1]}')
    if maius != '':
        print(f'MAIUSCULA\n{maius[:-1]}')
    if minus != '':
        print(f'MINUSCULA\n{minus[:-1]}')
    if pont != '':
        print(f'PONTUACAO\n{pont[:-1]}')

# print(f'MAIUSCULA\n{maius[:-1]}\nMINUSCULA\n{minus[:-1]}\nINFORMAL\n{informal[:-1]}\nPONTUAÇÃO\n{pont[:-1]}')
