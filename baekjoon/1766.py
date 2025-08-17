# https://www.acmicpc.net/problem/1766

import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # adjacency list
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

"""
print(graph)
[[], [], [], [1], [2]]

print(indegree)
[0, 1, 1, 0, 0]
"""

# put all nodes with indegree 0 into a min-heap
# ensures the smallest-numbered problem is chosen first
heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

"""
print(heap)
[3, 4]
"""

order = []
while heap:
    current = heapq.heappop(heap)
    order.append(current)  # order.append(3)
    for neighbor in graph[current]:  # for 1 in [1]:
        indegree[neighbor] -= 1  # indegree[1] -= 1
        if indegree[neighbor] == 0:
            heapq.heappush(heap, neighbor)

print(*order)
