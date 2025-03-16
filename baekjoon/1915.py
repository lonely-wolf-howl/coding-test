# 가장 큰 정사각형
# https://www.acmicpc.net/problem/1915

import sys

input = sys.stdin.readline

# dp[i][j]
# (i, j)를 오른쪽 아래 꼭짓점으로 하는 가장 큰 정사각형의 한 변 길이


def largest_square(n, m, matrix):
    dp = [[0] * m for _ in range(n)]
    max_side = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().strip()))
    matrix.append(row)

print(largest_square(n, m, matrix))
