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

while True:
    try:
        str = input()

        for i in range(0,len(str)):
            if i == len(str)-1:
                break
            elif ord(str[i]) == 32:
                continue
            else:
                if ord(str[i]) in range(97,123):    #minusculo
                    j = 1
                    while ord(str[i+j]) == 32:
                        j += 1
                    
                    if ord(str[i+j]) in range(97,123):  #proximo minusculo
                        str = wordreplacer(str,i+j,chr(ord(str[i+j])-32))   #transforma MAIUSCULO
                
                else:   #MAIUSCULO
                    if ord(str[i+1]) in range(65,91):  #proximo MAIUSCULO
                        str = wordreplacer(str,i+1,chr(ord(str[i+1])+32))   #transforma minusculo
    
        print(str)
    
    except EOFError:
        break
