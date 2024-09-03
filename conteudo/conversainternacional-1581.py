n = int(input())

for _ in range(0,n):
    m = int(input())
    auxlang = ''
    inglesF = False

    for i in range(0,m):
        if i == 0:
            lang = input()
            continue

        auxlang = lang
        lang = input()
        
        if auxlang == lang:
            continue
        else:
            inglesF = True
    
    if inglesF == True:
        print('ingles')
    else:
        print(lang)
