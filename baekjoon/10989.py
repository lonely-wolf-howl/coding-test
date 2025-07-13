# https://www.acmicpc.net/problem/10989

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
