n = int(input())

for _ in range(n):
    freq = {}
    str = input()
    for let in str:
        if let.isalpha() == True:
            if let.isupper() == True:
                let = let.lower()
            if let not in freq:
                freq[let] = 1
            else:
                freq[let] += 1

    freq_max = []
    aux = []
    aux.append(max(freq.items(),key=lambda x:x[1]))
    for ele in freq.items():
        if ele[1] == aux[0][1]:
            freq_max.append(ele)
    
    aux = [x[0] for x in freq_max]
    aux.sort()
    for ele in aux:
        print(ele, end='')
    print()
