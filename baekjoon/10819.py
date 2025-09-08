# https://www.acmicpc.net/problem/10819

from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

max_diff = 0

for perm in permutations(nums, n):
    diff_sum = 0
    for i in range(n - 1):
        diff_sum += abs(perm[i] - perm[i + 1])
    max_diff = max(max_diff, diff_sum)

print(max_diff)
