# 파일 합치기
# https://www.acmicpc.net/problem/11066

"""
예제 입력
1
4
40 30 30 50
"""

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    file_sizes = [0] + list(map(int, input().split()))

    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i - 1] + file_sizes[i]

    # dp[i][j]: i번부터 j번까지 하나로 합치는데 필요한 최소 비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    for length in range(2, K + 1):
        for start in range(1, K - length + 2):
            end: int = start + length - 1
            min_cost = float("inf")

            for mid in range(start, end):
                cost: int = dp[start][mid] + dp[mid + 1][end]
                min_cost = min(min_cost, cost)

            dp[start][end] = min_cost + prefix_sum[end] - prefix_sum[start - 1]

    print(dp[1][K])
