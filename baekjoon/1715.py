# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    heapq.heappush(heap, x)

total_cost = 0

while len(heap) != 1:
    smallest = heapq.heappop(heap)
    next_smallest = heapq.heappop(heap)

    merge_cost = smallest + next_smallest
    total_cost += merge_cost

    heapq.heappush(heap, merge_cost)

print(total_cost)
