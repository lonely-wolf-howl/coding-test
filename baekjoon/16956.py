# 늑대와 양
# https://www.acmicpc.net/problem/16956

"""
예제 입력
6 6
..S...
..S.W.
.S....
..W...
...W..
......
"""

R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def is_within_bounds(x: int, y: int):
    return 0 <= x < R and 0 <= y < C


is_danger = False

for row in range(R):
    for col in range(C):
        if M[row][col] == "W":  # 늑대가 있는 위치를 찾음
            for direction in range(4):  # 4방향 탐색
                next_row = row + dx[direction]
                next_col = col + dy[direction]
                if not is_within_bounds(next_row, next_col):
                    continue
                if M[next_row][next_col] == "S":  # 늑대와 양이 인접
                    is_danger = True

if is_danger:
    print(0)  # 위험한 상태
else:
    print(1)  # 안전한 상태
    for row in range(R):
        for col in range(C):
            if M[row][col] == ".":  # 빈칸에 울타리 배치
                M[row][col] = "D"
    for row in M:
        print("".join(row))  # 배열을 문자열로 변환
