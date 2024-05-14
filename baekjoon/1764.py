# 듣보잡

"""
예제 입력
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

예제 출력
2
baesangwook
ohhenrie
"""

import sys

input = sys.stdin.readline

from collections import defaultdict

N, M = map(int, input().split())
name = [input().strip() for _ in range(N + M)]

# the dict is empty, but the first time a key is accessed, its value is initialized to 0.
dict = defaultdict(int)
answer = []

for x in name:
    dict[x] += 1

for key in dict:
    if dict[key] == 2:
        answer.append(key)
print(len(answer))

for x in sorted(answer):
    print(x)
