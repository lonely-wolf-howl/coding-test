# https://www.acmicpc.net/problem/9251

"""
예제 입력
ACAYKP
CAPCAK
"""

import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

n, m = len(a), len(b)

# dp[i][j] = lcs length for a[:i] and b[:j]
dp = []
for i in range(n + 1):
    row = []
    for j in range(m + 1):
        row.append(0)
    dp.append(row)

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1  # match extends lcs
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])  # skip one side

print(dp[n][m])

"""
  |        C    A    P    C    A    K
  |   0    0    0    0    0    0    0
A |   0    0    1    1    1    1    1
C |   0    1    1    1    2    2    2
A |   0    1    2    2    2    3    3
Y |   0    1    2    2    2    3    3
K |   0    1    2    2    2    3    4
P |   0    1    2    3    3    3    4
"""
