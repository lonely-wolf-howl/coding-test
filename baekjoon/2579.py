# https://www.acmicpc.net/problem/2579

import sys

input = sys.stdin.readline

n = int(input())
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = int(input().strip())

if n == 1:
    print(s[1])
    raise SystemExit
if n == 2:
    print(s[1] + s[2])
    raise SystemExit

# dp[i] = max score to reach stair 'i'
dp = [0] * (n + 1)

dp[0] = 0
dp[1] = s[1]
dp[2] = s[1] + s[2]

for i in range(3, n + 1):
    dp[i] = max(s[i] + dp[i - 2], s[i] + s[i - 1] + dp[i - 3])

print(dp[n])
