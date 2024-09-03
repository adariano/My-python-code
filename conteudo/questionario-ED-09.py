def tradutor(lib):
    ans = ''
    for key in lib.keys():
        ans += '{}'.format(key)* lib.get(key)
    return ans

count = int(input())
flag = False

for _ in range(count):
    lib = {}
    seq = input()
    ans = ''

    for i in range(len(seq)):
        if seq[i].isalpha() == True:
            lib[seq[i]] = 0
            term = ''
            for j in range(i+1,len(seq)):
                if seq[j].isnumeric() == True and j < len(seq)-1:
                    term += seq[j]
                elif seq[j].isnumeric() == True and j == len(seq)-1:
                    term += seq[j]
                    lib[seq[i]] = int(term)
                    break
                else:
                    lib[seq[i]] = int(term)
                    break
    
    print(tradutor(lib))
