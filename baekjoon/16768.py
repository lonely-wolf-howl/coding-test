# Mooyo Mooyo
# https://www.acmicpc.net/problem/16768


from collections import deque

N, K = map(int, input().split())
grid = [list(input()) for _ in range(N)]


def is_in_bounds(x: int, y: int, n: int, m: int):
    return 0 <= x < n and 0 <= y < m


def bfs(grid, x: int, y: int, n: int, k: int, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    color = grid[x][y]
    cells = [(x, y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if is_in_bounds(nx, ny, n, 10) and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cells.append((nx, ny))

    if len(cells) >= k:
        return cells

    return []


def apply_gravity(grid, n: int):
    for col in range(10):
        stack = []
        for row in range(n):
            if grid[row][col] != 0:
                stack.append(grid[row][col])

        for row in range(n - 1, -1, -1):  # range(start, stop, step)
            if stack:
                grid[row][col] = stack.pop()
            else:
                grid[row][col] = 0


def process(n: int, k: int, grid):
    while True:
        visited = [[False] * 10 for _ in range(n)]
        found = False

        for i in range(n):
            for j in range(10):
                if grid[i][j] != 0 and not visited[i][j]:
                    cells_to_remove = bfs(grid, i, j, n, k, visited)
                    if cells_to_remove:
                        found = True
                        for x, y in cells_to_remove:
                            grid[x][y] = 0

        if not found:
            break

        apply_gravity(grid, n)

    return grid


result = process(N, K, grid)

for row in result:
    print("".join(map(str, row)))
