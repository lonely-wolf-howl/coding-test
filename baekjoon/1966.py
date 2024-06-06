# 프린터 큐

"""
예제 입력
1
6 0
1 1 9 1 1 1
"""

import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())  # 1

for _ in range(test_case):
    N, M = list(map(int, input().split()))  # 6 0
    queue = list(map(int, input().split()))  # [1, 1, 9, 1, 1, 1]

    queue = deque([(priority, idx) for idx, priority in enumerate(queue)])
    # deque([(1, 0), (1, 1), (9, 2), (1, 3), (1, 4), (1, 5)])

    count = 0
    while True:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == M:
                print(count)  # 5
                break
