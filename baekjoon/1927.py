# https://www.acmicpc.net/problem/1927

import heapq

n = int(input())

heap = []
result = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)

for x in result:
    print(x)
