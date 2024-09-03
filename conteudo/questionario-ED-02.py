def frequencia (wor):
    freq = []
    dic = {i: 0 for i in wor}

    for i in wor:
        dic.update({i: dic.get(i) + 1})
    
    aux = 0
    ans = ''
    for i in dic:
        if dic.get(i) > aux:
            aux = dic.get(i)
            ans = i
    return ans