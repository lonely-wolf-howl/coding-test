# 배부른 마라토너

"""
예제 입력
3
leo
kiki
eden
eden
kiki
"""

import sys

input = sys.stdin.readline

from collections import Counter

N = int(input())
participants = [input().strip() for _ in range(N)]
completions = [input().strip() for _ in range(N - 1)]

dict = Counter(participants)
answer = ""

for x in completions:
    dict[x] -= 1

for key, value in dict.items():
    if value == 1:
        answer = key

print(answer)
