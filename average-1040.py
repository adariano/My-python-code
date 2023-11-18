n1,n2,n3,n4 = map(float,input().split())

med = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print(f'Media: {med:.1f}')

if med >= 7:
    print('Aluno aprovado.')

elif med >= 5 and med < 7:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    med_fin = (med + n5) / 2
    if med_fin >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {med_fin:.1f}')
else:
    print('Aluno reprovado.')