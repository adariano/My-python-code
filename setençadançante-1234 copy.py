while True:
    try:
        str = input()
        
        for i in range(len(str)):
            if i < len(str)-1:
                if str[i].isalpha() == True:
                    if str[i].isupper() == True:
                        str[i+1] = ''
                        str[i+1] = str[i+1].lower()
                    else: #minusculo
                        str[i+1] = ''
                        str[i+1] = str[i+1].upper()
                elif ord(str[i+1]) == 32:
                    cont = 0
                    while ord(str[i+cont]) == 32:
                        cont=+1
                    if str[i].isupper() == True:
                        if str[i+cont].isupper() == True:
                            str[i+cont].lower()

        print(str)
    except EOFError:
        break