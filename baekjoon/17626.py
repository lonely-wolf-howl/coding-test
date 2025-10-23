# https://www.acmicpc.net/problem/17626

import sys

from math import isqrt

input = sys.stdin.readline
n = int(input())

dp = [0] + [4] * n

for i in range(1, n + 1):
    r = isqrt(i)
    if r * r == i:
        dp[i] = 1
        continue

    for j in range(1, n):
        if j * j > i:
            break
        dp[i] = min(dp[i], 1 + dp[i - j * j])

print(dp[n])
