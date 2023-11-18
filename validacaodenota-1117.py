while True:
    x = float(input())

    if x >= 0 and x <= 10:
        break
    else:
        print('nota invalida')

while True:
    y = float(input())

    if y >= 0 and y <= 10:
        break
    else:
        print('nota invalida')

print(f'media = {(x + y)/2:.2f}')