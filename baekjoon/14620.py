# 꽃길
# https://www.acmicpc.net/problem/14620

"""
예제 입력
6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1
"""

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

answer = float("inf")

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]


def process(flower_positions):
    total_cost = 0
    visited = set()

    for position in flower_positions:
        # 1차원을 2차원으로 변환
        x: int = position // N  # 행 번호
        y: int = position % N  # 열 번호

        # 꽃 중심이 격자의 가장자리에 있으면 무효
        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return float("inf")

        # 꽃이 차지하는 5개의 칸을 처리
        for direction in range(5):
            nx: int = x + dx[direction]
            ny: int = y + dy[direction]

            # 이미 다른 꽃이 차지한 칸이면 무효
            if (nx, ny) in visited:
                return float("inf")

            # 방문 처리 및 비용 계산
            visited.add((nx, ny))
            total_cost += M[nx][ny]

    return total_cost


# 모든 꽃 배치의 가능한 조합을 탐색
for i in range(N * N):
    for j in range(i + 1, N * N):
        for k in range(j + 1, N * N):
            flower_positions = [i, j, k]
            answer = min(answer, process(flower_positions))

print(answer)
