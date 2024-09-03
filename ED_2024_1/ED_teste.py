def dekey(x):
    lista3 = []
    for i in x:
        lista3.append(i)
    re = int(lista3[2]) 
    lista3.pop(0)
    lista3.pop(0)
    
    lista3.pop(0)
    while re != 0:
        if lista3[0] < lista3[1]:
            lista3.append(lista3[0])
            lista3.pop(0)
        else:
            lista3.append(lista3[1])
            lista3.pop(1)  
        re -= 1   
    y = "".join(lista3)        
        
    
    return y
   

def scramble(x):
    #a cada ( o proximo a te um ( ou ) fica em primeiro, e depois do ) lanca o proximo ate o ( ou ) para o final
    li = []
    x.pop(0)
    x.pop(0)
    x = "".join(x)
    li = x.split("(")
    #tem q ter o caso de nao ter "("
    li2 = []
    for i in li:
        if ")" not in i:
            li2.insert(0,i)
        else:
            listinha = []
            listinha = i.split(")")
            li2.insert(0,listinha[0])
            li2.append(listinha[len(listinha) - 1])
    z = "".join(li2)           
    
    return z
    
    
lista = []
plista = ["","","","","",""]
lista2 = []
x = True

while x == True:
    
    lista = input().split()
    if lista[0] == "enqueue":
        for i in range(int(lista[1])):
            lista2 = input().split()
            if lista2[1] == "dekey":
                plista.insert(int(lista2[0]),dekey(lista2))
            if lista2[1] == "scramble":
                plista.insert(int(lista2[0]),scramble(lista2))
    #for i in range(len(plista) - 1):
        #if plista[i] == '':
            #plista.pop(i)    
    if lista[0] == "go":
        for i in range(len(plista)):
            if plista[i] != '':
                print(plista[i])
                plista.pop(i)
                break
            
                
                break
    if lista[0] == "stop":
        contador = 0
        for i in range(len(plista)):
            if plista[i] != '':
                contador = contador + 1
                
        print(f"{contador} processo(s) órfão(s).")
        x = False