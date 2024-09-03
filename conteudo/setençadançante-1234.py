def wordreplacer(string,pos,new):
    new_string = ''
    index = 0

    while index < len(string):
        if index == pos:
            new_string = new_string + new
        else:
            new_string += string[index]
        index += 1
    return new_string

def checkUpCase(str):
    if ord(str) in range(65,91):
        return True
    else:
        return False

def checkLowCase(str):
    if ord(str) in range(97,123):
        return True
    else:
        return False

while True:
    try:
        str = input()

        for i in range(len(str)):
            if i != len(str)-1:
                if checkUpCase(str[i]) == True and ord(str[i+1]) == 32: #MAISUCULOe MAIUSCULO espaçado
                    aux = 1
                    while True:
                        if ord(str[i+aux]) != 32:
                            break
                        aux+=1
                    if checkUpCase(str[i+aux]) == True:
                        str = wordreplacer(str,i+aux,chr(ord(str[i+aux])+32))

                elif checkLowCase(str[i]) == True and ord(str[i+1]) == 32: #minusculo e minusculo espacado
                    aux = 1
                    while True:
                        if ord(str[i+aux]) != 32:
                            break
                        aux+=1
                    if checkLowCase(str[i+aux]) == True:
                        str = wordreplacer(str,i+aux,chr(ord(str[i+aux])-32))

                elif checkUpCase(str[i]) == True and checkUpCase(str[i+1]) == True: # MAIUSCULO e MAIUSCULO
                   str = wordreplacer(str,i+1,chr(ord(str[i+1])+32))
                elif checkLowCase(str[i]) == True and checkLowCase(str[i+1]) == True: # minusculo e minusculo
                    str = wordreplacer(str,i+1,chr(ord(str[i+1])-32))

        print(str)
    except EOFError:
        break
