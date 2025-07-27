# https://www.acmicpc.net/problem/1939

from collections import deque


# check path exists with limit weight
def bfs(limit):
    visited = [False] * (n + 1)
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        current = queue.popleft()
        for neighbor, weight in graph[current]:
            if not visited[neighbor] and weight >= limit:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited[end_node]


# input
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # adjacency list
min_w, max_w = int(1e9), 0

for _ in range(m):
    x, y, limit = map(int, input().split())
    graph[x].append((y, limit))
    graph[y].append((x, limit))
    min_w = min(min_w, limit)
    max_w = max(max_w, limit)

start_node, end_node = map(int, input().split())

# binary search
result = min_w
left, right = min_w, max_w

while left <= right:
    mid = (left + right) // 2  # current weight
    if bfs(mid):  # if reachable with current weight
        result = mid
        left = mid + 1  # try higher weight
    else:
        right = mid - 1  # try lower weight

print(result)
