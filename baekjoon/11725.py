# https://www.acmicpc.net/problem/11725

import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
parents = [0] * (n + 1)

# graph
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

stack = [1]
visited[1] = True

while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parents[neighbor] = node  # set parent
            stack.append(neighbor)

for i in range(2, n + 1):
    print(parents[i])
