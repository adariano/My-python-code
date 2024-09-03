cont =int(input())

for _ in range(cont):
    seq = input()
    aux = 0

    for i in range(len(seq)):
        #se achar um 1
        if seq[i] == '1':
            #começe com o proximo termo
            for j in range(i+1, len(seq)-1):
                flag = False

                #checar se existe um 1 nos proximos termos, e se sim flag=True
                for k in range(j,len(seq)):
                    if seq[k] == '1':
                        flag = True
    
                #checar se o proximo termo é um zero e penultimo
                if seq[j] == '0' and j < len(seq) and flag == True:
                    aux += 1
                else:
                    break
    
    print(aux)

