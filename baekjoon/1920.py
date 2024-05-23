# 수 찾기

"""
예제 입력
5
4 1 5 2 3
5
1 3 7 9 5
"""

import sys

input = sys.stdin.readline

N = int(input())
N_SET = set(map(int, input().split()))
M = int(input())
M_ARR = list(map(int, input().split()))

for x in M_ARR:
    if x not in N_SET:
        print("0")
    else:
        print("1")

# A dict stores key-value pairs and retrieves values through their keys.
# A set stores only unique values and checks for the existence of values directly.
