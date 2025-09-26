# https://www.acmicpc.net/problem/5567

from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph
# [[], [2, 3], [1, 3], [1, 4, 2], [3, 5], [4], []]

dist = [-1] * (n + 1)
dist[1] = 0

queue = deque([1])  # start from node 1
while queue:
    node = queue.popleft()
    if dist[node] == 2:
        continue
    for neighbor in graph[node]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[node] + 1
            queue.append(neighbor)

# dist
# [-1, 0, 1, 1, 2, -1, -1]

invite_count = 0
for d in dist:
    if 1 <= d <= 2:
        invite_count += 1

print(invite_count)
