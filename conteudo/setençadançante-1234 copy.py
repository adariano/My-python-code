strlist = []

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
        for str in strlist:
            for i in range(len(str)):
                if i == len(str)-1:
                    break
                if str[i].isupper() ==  True:
                    if ord(str[i+1]) == 32: 
                        cont = 1
                        while ord(str[i+cont]) == 32:
                            cont+=1
                        if str[i+cont].upper() == True:
                            str = replaceChar(str,i+cont,str[i+cont].lower())
                    elif str[i+1].isupper() == True:
                        str = replaceChar(str,i+1,str[i+1].lower())
                else:
                    if ord(str[i+1]) == 32: 
                        cont = 1
                        while ord(str[i+cont]) == 32 and i+cont < len(str)-1:
                            cont+=1
                        if str[i+cont].lower() == True:
                            str = replaceChar(str,i+cont,str[i+cont].upper())
                    elif str[i+1].islower() == True:
                        str = replaceChar(str,i+1,str[i+1].upper())
            print(str)

        break