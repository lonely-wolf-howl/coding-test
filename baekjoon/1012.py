# 유기농 배추
# https://www.acmicpc.net/problem/1012

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x: int, y: int, grid: list, visited: list):
    visited[x][y] = True
    # 네 방향 탐색
    for i in range(4):
        # 새로운 좌표 계산
        nx, ny = x + dx[i], y + dy[i]
        if not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny, grid, visited)


def process():
    M, N, K = map(int, input().split())

    # 여백을 추가하여 격자 생성
    grid = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]

    # 배추 위치 입력 (여백 때문에 +1씩 더해줌)
    for _ in range(K):
        X, Y = map(int, input().split())
        # 배추가 있는 위치 표시 (Y+1, X+1)
        grid[Y + 1][X + 1] = 1

    # 연결 요소의 개수 (필요한 지렁이 수)
    answer = 0

    # 여백이 추가된 격자를 순회하며 DFS 실행
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, grid, visited)
                answer += 1

    print(answer)


for _ in range(T):
    process()
