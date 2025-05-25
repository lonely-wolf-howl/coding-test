# 전쟁 - 전투
# https://www.acmicpc.net/problem/1303

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * N for _ in range(M)]


def dfs_stack(x, y, team):
    stack = [(x, y)]
    visited[y][x] = True
    count = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx: int = cx + dx[i]
            ny: int = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[ny][nx] and grid[ny][nx] == team:
                    visited[ny][nx] = True
                    stack.append((nx, ny))
                    count += 1

    return count


w_score = 0
b_score = 0

for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            team: str = grid[y][x]
            group_size: int = dfs_stack(x, y, team)
            if team == "W":
                w_score += group_size**2
            else:
                b_score += group_size**2

print(w_score, b_score)
