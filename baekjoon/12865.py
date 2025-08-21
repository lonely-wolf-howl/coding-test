# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(0, K + 1):
        dp[i][w] = dp[i - 1][w]
        if w >= weight:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

print(dp[N][K])
