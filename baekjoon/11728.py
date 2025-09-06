# https://www.acmicpc.net/problem/11728

import sys

read = sys.stdin.readline

n, m = map(int, read().split())

a = list(map(int, read().split()))
b = list(map(int, read().split()))

i = j = 0
c = []

while i < n and j < m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

if i < n:
    c.extend(a[i:])
if j < m:
    c.extend(b[j:])

print(" ".join(map(str, c)))
