# https://www.acmicpc.net/problem/11726

n = int(input())

mod = 10007

dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2

# dp[i]: ways to tile 2×i
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n])
