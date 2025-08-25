# https://www.acmicpc.net/problem/1495

N, S, M = map(int, input().split())
changes = list(map(int, input().split()))

# dp[i][v]: i번째 곡을 v로 연주가 가능한지 여부
dp = []
for i in range(N + 1):
    row = []
    for v in range(M + 1):
        row.append(False)
    dp.append(row)

if 0 <= S <= M:
    dp[0][S] = True

for i in range(1, N + 1):
    delta = changes[i - 1]  # 이번 곡에서 + 또는 - 할 수 있는 값
    for v in range(M + 1):
        if dp[i - 1][v]:
            nv = v + delta
            if 0 <= nv <= M:
                dp[i][nv] = True
            nv = v - delta
            if 0 <= nv <= M:
                dp[i][nv] = True

answer = -1
for v in range(M, -1, -1):
    if dp[N][v]:
        answer = v
        break
print(answer)
