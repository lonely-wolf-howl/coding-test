# DFS와 BFS
# https://www.acmicpc.net/problem/1260

"""
예제 입력
4 5 1
1 2
1 3
1 4
2 4
3 4
"""

from collections import deque


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))

    return " ".join(map(str, visited))


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))

    return " ".join(map(str, visited))


def build_adjacency_list(n, edges):
    adj_list = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    adj_list = build_adjacency_list(N, edges)

    print(dfs(adj_list, V))
    print(bfs(adj_list, V))
