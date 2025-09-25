# https://www.acmicpc.net/problem/2606

from collections import deque

node_count = int(input())
edge_count = int(input())

adjacency_list = [[] for _ in range(node_count)]

for _ in range(edge_count):
    u, v = map(int, input().split())
    adjacency_list[u - 1].append(v - 1)
    adjacency_list[v - 1].append(u - 1)

visited = [False] * node_count
visited[0] = True  # start node (computer 1)

# breadth first search
queue = deque([0])
while queue:
    current = queue.popleft()
    for neighbor in adjacency_list[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

connected_count = 0
for node_index in range(1, node_count):
    if visited[node_index] == 1:
        connected_count += 1

connected_count = sum(visited) - 1
print(connected_count)
