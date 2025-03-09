# 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055

"""
예제 입력
10
1 100 2 50 60 3 5 6 7 8
"""

import copy

N = int(input())
A = list(map(int, input().split()))

DP = copy.deepcopy(A)

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + A[i])

print(max(DP))
