# 듣보잡
# https://www.acmicpc.net/problem/1764

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
"""

from collections import defaultdict

N, M = map(int, input().split())
name = [input().strip() for _ in range(N + M)]

# the name_count is empty, but the first time a key is accessed,
# its value is initialized to 0
name_count = defaultdict(int)
answer = []

for x in name:
    name_count[x] += 1

for key in name_count:
    if name_count[key] == 2:
        answer.append(key)

print(len(answer))

for x in sorted(answer):
    print(x)
