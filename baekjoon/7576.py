# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())

box = []
for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)

# up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

# breadth-first search
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # check bounds and unripe tomatoes
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

max_day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:  # unripe tomato remains
            print(-1)
            exit(0)
        if box[i][j] > max_day:
            max_day = box[i][j]

print(max_day - 1)
