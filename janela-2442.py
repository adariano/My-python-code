f1,f2,f3 = map(int,input().split())

area_t = 60000

#tinha que colocar as variáveis EM ORDEM lmaooooooo :clown:

if f1 > f2:
    aux = f1
    f1 = f2
    f2 = aux

if f2 > f3:
    aux = f2
    f2 = f3
    f3 = aux

if f1 > f2:
    aux = f1
    f1 = f2
    f2 = aux

#as tres janelas juntas
if f2 < (f1 + 200) and f3 < (f2 + 200):
    area_o = ((f3 + 200) - f1)*100
    area_a = area_t - area_o
    print(area_a)
#as janelas f1 e f2 juntas, e f3 separada
elif f2 < (f1 + 200) and f3 > (f2 + 200):
    area_o = ((f2 + 200 - f1) + 200)*100
    area_a = area_t - area_o
    print(area_a)
#as janelas f1 separada, e f2 e f3 juntas
elif f2 > (f1 + 200) and f3 < (f2 + 200):
    area_o = (200 + (f3 + 200) - f2)*100
    area_a = area_t - area_o
    print(area_a)
#e por fim todas as janelas separadas
else:
    print('0')
    