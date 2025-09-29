# https://www.acmicpc.net/problem/1012

t = int(input())

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
    m, n, k = map(int, input().split())

    grid = [[0 for i in range(m + 2)] for j in range(n + 2)]
    visited = [[False for i in range(m + 2)] for j in range(n + 2)]

    for _ in range(k):
        x, y = map(int, input().split())
        grid[y + 1][x + 1] = 1

    answer = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, grid, visited)
                answer += 1

    print(answer)


for i in range(t):
    process()
