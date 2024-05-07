# 회전하는 큐

"""
예제 입력
10 3
1 2 3
"""

import sys

input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))

deq = deque([i for i in range(1, N + 1)])  # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
count = 0

for target in targets:
    index = deq.index(target)  # if target is '1' then index is '0'

    if index <= len(deq) // 2:
        for i in range(index):  # 'for i in range(0)' does not execute
            deq.append(deq.popleft())
            count += 1
    else:
        for i in range(len(deq) - index):
            deq.appendleft(deq.pop())
            count += 1
    deq.popleft()

print(count)
