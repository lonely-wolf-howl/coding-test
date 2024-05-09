# 요세푸스 문제 0

"""
예제 입력
7 3
"""

import sys

input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
deq = deque([i for i in range(1, N + 1)])

result = []

for i in range(N):
    for i in range(K - 1):  # rotate clockwise 'K' times
        x = deq.popleft()
        deq.append(x)

    x = deq.popleft()  # extract element
    result.append(x)

print("<", end="")
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=", ")
    else:
        print(result[i], end="")
print(">")

# 1 2 3 4 5 6 7

# 1 2 - 4 5 6 7 = 3
# 1 2   4 5 - 7 = 6
# 1 -   4 5   7 = 2
# 1     4 5   - = 7
# 1     4 -     = 5
# -     4       = 1
#       -       = 4
