# https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())

deq = deque(list(range(1, n + 1)))

drop = True

while len(deq) > 1:
    if drop:
        deq.popleft()
        drop = False
    else:
        x = deq.popleft()
        deq.append(x)
        drop = True

print(deq[0])
