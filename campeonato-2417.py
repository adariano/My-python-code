c_vit,c_emp,c_sal,f_vit,f_emp,f_sal = map(int,input().split())

def pontos (vit,emp):
    total = (vit * 3) + (emp)
    return total

c_pon = pontos(c_vit,c_emp)
f_pon =  pontos(f_vit,f_emp)

if c_pon != f_pon:
    if c_pon > f_pon:
        print("C")
    else:
        print("F")
else:
    if c_sal != f_sal:
        if c_sal > f_sal:
            print('C')
        else:
            print('F')
    else:
        print("=")