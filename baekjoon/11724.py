# https://www.acmicpc.net/problem/11724

import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = list(map(int, input().split()))

    graph[a].append(b)
    graph[b].append(a)

# graph
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if visited[i]:
        continue

    count += 1  # found a new connected component

    # breadth first search
    queue = deque([i])
    visited[i] = True

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

print(count)
