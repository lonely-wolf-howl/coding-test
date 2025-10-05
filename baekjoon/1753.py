# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = float("inf")

# adjacency list
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# dijkstra algorithm
dist = [INF] * (V + 1)
dist[K] = 0

heap = [(0, K)]

while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    if cur_dist > dist[cur_node]:
        continue

    for nxt_node, weight in graph[cur_node]:
        can_dist = cur_dist + weight
        if can_dist < dist[nxt_node]:
            dist[nxt_node] = can_dist
            heapq.heappush(heap, (can_dist, nxt_node))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
