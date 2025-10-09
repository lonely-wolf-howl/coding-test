# https://www.acmicpc.net/problem/1766

import sys
from queue import PriorityQueue

input = sys.stdin.readline

n, m = map(int, input().split())

# number of incoming edges to node 'i'
indegree = [0] * (n + 1)

adj = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

# adj
# [[], [], [], [1], [2]]

# indegree
# [0, 1, 1, 0, 0]

pq = PriorityQueue()
for i in range(1, n + 1):
    if indegree[i] == 0:
        pq.put(i)

# topological sort
order = []
while pq.qsize() != 0:
    u = pq.get()
    order.append(u)

    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            pq.put(v)

print(*order)
