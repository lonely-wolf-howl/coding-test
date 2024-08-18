# 블랙잭

"""
예제 입력
5 21
5 6 7 8 9
"""

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))

result = 0
length = len(data)

for a in range(0, length):
    for b in range(a + 1, length):
        for c in range(b + 1, length):
            sum = data[a] + data[b] + data[c]
            if sum <= M:
                result = max(result, sum)

print(result)
