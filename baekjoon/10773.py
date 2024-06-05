# 제로

"""
예제 입력
4
3
0
4
0
"""

import sys

input = sys.stdin.readline

K = int(input())

stack = []

for _ in range(K):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)

print(sum(stack))
