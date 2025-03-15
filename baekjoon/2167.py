# 2차원 배열의 합
# https://www.acmicpc.net/problem/2167

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * (M + 1) for _ in range(N + 1)]

"""
00 00 00 00
00 00 00 00
00 00 00 00
"""

for i in range(1, N + 1):
    for j in range(1, M + 1):
        DP[i][j] = arr[i - 1][j - 1] + DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1]

"""
00 00 00 00
00 01 03 07
00 09 27 63
"""

K = int(input())
for _ in range(K):
    i1, j1, i2, j2 = map(int, input().split())

    result = DP[i2][j2] - DP[i1 - 1][j2] - DP[i2][j1 - 1] + DP[i1 - 1][j1 - 1]
    print(result)
