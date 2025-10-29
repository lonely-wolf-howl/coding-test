# https://www.acmicpc.net/problem/1759

from itertools import combinations

l, c = map(int, input().split())
a = input().split()

a.sort()

v = {"a", "e", "i", "o", "u"}

for comb in combinations(a, l):
    vc = 0
    cc = 0

    for ch in comb:
        if ch in v:
            vc += 1
        else:
            cc += 1

    if vc >= 1 and cc >= 2:
        print("".join(comb))
