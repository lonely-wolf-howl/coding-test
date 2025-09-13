# https://www.acmicpc.net/problem/2559

n, k = map(int, input().split())
temps = list(map(int, input().split()))

prefix = [0] * n
prefix[0] = temps[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + temps[i]

window_sums = []

for i in range(0, n - k + 1):
    if i == 0:
        window_sum = prefix[i + k - 1]
    else:
        window_sum = prefix[i + k - 1] - prefix[i - 1]

    window_sums.append(window_sum)

print(max(window_sums))
