# https://www.acmicpc.net/problem/15650

from itertools import combinations

n, m = map(int, input().split())

for com in combinations(range(1, n + 1), m):
    print(*com)
