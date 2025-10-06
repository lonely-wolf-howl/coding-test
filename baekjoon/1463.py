# https://www.acmicpc.net/problem/1463

n = int(input())

# dp[i] = min number of operations to make i → 1
dp = [0] * (n + 1)

dp[1] = 0

for i in range(2, n + 1):
    dp[i] = 1 + dp[i - 1]

    if i % 3 == 0:
        dp[i] = min(dp[i], 1 + dp[i // 3])
    if i % 2 == 0:
        dp[i] = min(dp[i], 1 + dp[i // 2])

print(dp[n])
