import math

def escapar (posr,posc,posb):
    distc = math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(posc, posb)))
    distr = math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(posr, posb)))
    #se vai escapar, então true
    if distc*2 >= distr:
        return True
    else:
        return False

bur = (int(input()))
posc = [float(i) for i in input().split()]
posr = [float(i) for i in input().split()]

for n in range(bur):
    buraux = [float(i) for i in input().split()]
    escflag = escapar(posr,posc,buraux)
    
    if escflag == False:
        print(f'O coelho pode escapar pelo buraco ({buraux[0]:.3f}, {buraux[1]:.3f}).')
        break
    else:
        if n+1 == bur:
            print('O coelho nao pode escapar.')
        continue

