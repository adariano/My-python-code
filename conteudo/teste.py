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
  
str = 'abcdef'

str = replaceChar(str,2,'C')
print(str)