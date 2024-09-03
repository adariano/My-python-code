strlist = []
switch = 0

def replaceChar(str,index,replaceChar):
    new_str = ''
    cont = 0
    while cont < len(str):
        if cont == index:
            new_str += replaceChar
        else:
            new_str += str[cont]        
        cont+=1
    return new_str

while True:
    try:
        str = input()
        strlist.append(str)
        # print(strlist)

    except EOFError:
        for pal in strlist:
            flag = False
            case = 0
            for i in range(len(pal)):
                if ord(pal[i]) != 32:
                    if pal[i].islower == True and flag == False: # Primeira letra minuscula para MAIUSCULA / Só uma vez
                        pal = replaceChar(pal,i,pal[i].upper())
                        case = 1
                        flag == True
                    elif case == 0:
                        pal = replaceChar(pal,i,pal[i].upper())
                        flag = True
                        case = 1
                    elif case == 1:
                        pal = replaceChar(pal,i,pal[i].lower())
                        flag = True
                        case = 0
            print(pal)
        break