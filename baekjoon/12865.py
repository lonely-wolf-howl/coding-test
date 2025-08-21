# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = []
for i in range(N + 1):
    row = []
    for j in range(K + 1):
        row.append(0)
    dp.append(row)

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(0, K + 1):
        dp[i][w] = dp[i - 1][w]
        if w >= weight:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

print(dp[N][K])

"""
    | w=0  w=1  w=2  w=3  w=4  w=5  w=6  w=7
i=0 |   0    0    0    0    0    0    0    0
i=1 |   0    0    0    0    0    0   13   13
i=2 |   0    0    0    0    8    8   13   13
i=3 |   0    0    0    6    8    8   13   14
i=4 |   0    0    0    6    8   12   13   14
"""
