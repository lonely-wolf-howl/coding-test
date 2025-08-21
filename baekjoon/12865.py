# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))  # (무게, 가치)

# dp[i][w] = i번째 물건까지 고려했을 때, 용량 w에서의 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(0, K + 1):
        # i번째 물건을 안 담는 경우
        dp[i][w] = dp[i - 1][w]
        # i번째 물건을 담을 수 있는 경우
        if w >= weight:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

print(dp[N][K])
