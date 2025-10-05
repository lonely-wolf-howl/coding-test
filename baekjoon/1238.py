# https://www.acmicpc.net/problem/1238

import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

INF = float("inf")

# adjacency lists
adj = [[] for i in range(n + 1)]
reversed_adj = [[] for j in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    reversed_adj[v].append((u, w))


def dijkstra(start, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        cur_dist, cur_node = heapq.heappop(min_heap)

        if cur_dist > dist[cur_node]:
            continue

        for nxt_node, weight in graph[cur_node]:
            can_dist = cur_dist + weight
            if can_dist < dist[nxt_node]:
                dist[nxt_node] = can_dist
                heapq.heappush(min_heap, (can_dist, nxt_node))
    return dist


# distances from x to all nodes
dist_from = dijkstra(x, adj)

# distances to x from all nodes
dist_to = dijkstra(x, reversed_adj)

max_trip = 0
for i in range(1, n + 1):
    trip = dist_to[i] + dist_from[i]
    if trip > max_trip:
        max_trip = trip

print(max_trip)
