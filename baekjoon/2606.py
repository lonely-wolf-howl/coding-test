# https://www.acmicpc.net/problem/2606

n = int(input())
e = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(e):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def dfs(node):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)


dfs(1)

count = 0
for i in range(2, n + 1):
    if visited[i]:
        count += 1

print(count)
