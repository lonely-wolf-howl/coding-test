# 오큰수

"""
예제 입력
4
3 5 2 7
"""

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

NGE = [-1] * N

stack = []

for i in range(N):
    current = A[i]

    while stack and (stack[-1][0] < current):
        stack_value, stack_index = stack.pop()
        NGE[stack_index] = current

    stack.append((current, i))

print(*NGE)
