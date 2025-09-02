# https://www.acmicpc.net/problem/2343

n, m = map(int, input().split())
times = list(map(int, input().split()))

left, right = max(times), sum(times)
answer = -1

while left <= right:
    mid = (left + right) // 2  # candidate capacity
    used = 1  # number of discs used
    remain = mid

    for time in times:
        if remain < time:
            used += 1
            remain = mid  # reset to full capacity
        remain -= time

    if used <= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
