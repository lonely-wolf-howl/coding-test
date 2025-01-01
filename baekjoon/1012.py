# 유기농 배추
# https://www.acmicpc.net/problem/1012

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x: int, y: int, grid: list, visited: list):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))


def process():
    M, N, K = map(int, input().split())

    grid = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]

    for _ in range(K):
        X, Y = map(int, input().split())
        grid[Y + 1][X + 1] = 1

    answer = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, grid, visited)
                answer += 1

    print(answer)


for _ in range(T):
    process()
