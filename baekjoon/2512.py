# https://www.acmicpc.net/problem/2512

n = int(input())

requests = list(map(int, input().split()))
total_budget = int(input())

left = 0
right = max(requests)

answer = -1

while left <= right:
    mid = (left + right) // 2  # candidate upper limit
    allocated = 0
    for i in range(n):
        allocated += min(mid, requests[i])

    if allocated <= total_budget:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
