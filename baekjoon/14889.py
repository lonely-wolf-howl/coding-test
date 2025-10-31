# https://www.acmicpc.net/problem/14889

from itertools import combinations

n = int(input())
s = [[] for i in range(n)]

for i in range(n):
    s[i] = list(map(int, input().split()))

min_diff = 1e9

for a in combinations(range(n), n // 2):
    b = []
    for i in range(n):
        if i not in a:
            b.append(i)

    # a = (0, 1)
    # b = [2, 3]

    a_power = 0
    b_power = 0

    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                a_power += s[a[i]][a[j]]

    for i in range(len(b)):
        for j in range(len(b)):
            if i != j:
                b_power += s[b[i]][b[j]]

    diff = abs(a_power - b_power)
    min_diff = min(min_diff, diff)

    if min_diff == 0:
        break

print(min_diff)
