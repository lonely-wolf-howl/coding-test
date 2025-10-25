# https://www.acmicpc.net/problem/1182

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for r in range(1, n + 1):  # r: subset length
    for comb in combinations(arr, r):
        if sum(comb) == s:
            cnt += 1

print(cnt)
