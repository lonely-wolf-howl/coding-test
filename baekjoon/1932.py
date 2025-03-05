# 정수 삼각형
# https://www.acmicpc.net/problem/1932

"""
예제 입력
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

N = int(input())
A = [[0 for _ in range(N + 1)] for i in range(N + 1)]

# 각 위치에 도달할 때의 최대 합을 저장
DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(1, i + 1):
        A[i][j] = temp[j - 1]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        # 점화식
        DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]

print(max(DP[-1]))
