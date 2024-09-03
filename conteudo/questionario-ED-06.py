import math

tam = int(input())
counttotal = transmitido = countlocal = 0
print(f'Transmitindo {tam} bytes...')

while tam > 0:
    transmissao = int(input())
    counttotal += 1
    countlocal += 1
    tam -= transmissao
    transmitido += transmissao

    if counttotal % 5 == 0 and tam > 0:
        if transmitido == 0:
            print('Tempo restante: pendente...')
            continue
        ans = 'Tempo restante: ' + str(math.ceil((tam) / (transmitido / 5))) + ' segundos.'
        print(ans)
        transmitido = 0
        countlocal = 0

print(f'Tempo total: {counttotal} segundos.')