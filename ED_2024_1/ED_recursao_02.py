from pythonds.basic import Deque

def dequeCheck(deq,soma = 0,ans = 0):
    if deq.isEmpty() == False:
        dequeCheck(deq,soma + deq.removeFront(),ans)
        dequeCheck(deq,soma + deq.removeRear(),ans)
    else:
        if soma > ans:
            ans = soma

x = input()
deq = Deque()
for item in [int(x) for x in input().split()]:
    deq.addFront(item)
print(dequeCheck(deq))

print(deq)