# https://www.acmicpc.net/problem/14465

n, k, b = map(int, input().split())

broken = [0] * n

for _ in range(b):
    idx = int(input())
    broken[idx - 1] = 1

# broken
# [1, 1, 0, 0, 1, 0, 0, 0, 1, 1]

prefix = [0] * n
prefix[0] = broken[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + broken[i]

# prefix
# [1, 2, 2, 2, 3, 3, 3, 3, 4, 5]

window_sums = []

for i in range(0, n - k + 1):
    if i == 0:
        window_sum = prefix[i + k - 1]
    else:
        window_sum = prefix[i + k - 1] - prefix[i - 1]

    window_sums.append(window_sum)

# window_sums
# [3, 2, 1, 2, 3]

print(min(window_sums))
