# https://www.acmicpc.net/problem/2805

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))

# binary search
low = 0
high = max(h)

answer = -1
while low <= high:
    mid = (low + high) // 2

    total = 0
    for i in range(n):
        if h[i] > mid:
            total += h[i] - mid

    if total >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
