# https://www.acmicpc.net/problem/21318

import sys

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))
q = int(input().strip())

drops = [0] * n
i = 1
while i < n:
    drops[i] = drops[i - 1]
    if a[i - 1] > a[i]:
        drops[i] = drops[i] + 1
    i += 1

# drops
# [0, 0, 0, 0, 0, 1, 1, 2, 3]

t = 0
while t < q:
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(drops[b - 1] - drops[a - 1])
    t += 1
