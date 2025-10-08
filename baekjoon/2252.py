# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# number of incoming edges to node 'i'
indegree = [0] * (n + 1)

adj = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

# topological sort
order = []
while q:
    u = q.popleft()
    order.append(u)

    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

print(*order)
