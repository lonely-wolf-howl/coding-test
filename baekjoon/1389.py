# https://www.acmicpc.net/problem/1389

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

best_sum = 1e9
best_person = -1

for start in range(1, n + 1):
    visited = [False] * (n + 1)
    dist = [-1] * (n + 1)

    # breadth first search from start
    q = deque([start])
    visited[start] = True
    dist[start] = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    total = sum(dist)

    if total < best_sum:
        best_sum = total
        best_person = start

print(best_person)
