# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input().strip())))

visited = [[False] * m for j in range(n)]
dist = [[0] * m for k in range(n)]

queue = deque([(0, 0)])

visited[0][0] = True
dist[0][0] = 1

# up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    r, c = queue.popleft()

    if r == n - 1 and c == m - 1:
        print(dist[r][c])
        break

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
