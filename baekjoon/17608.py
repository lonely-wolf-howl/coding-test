# 막대기

"""
예제 입력
6
6
9
7
6
4
6
"""

import sys

input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]


def solution(heights):
    answer = 0
    max_height = 0

    # N = 6, i = 5, 4, 3, 2, 1, 0
    for i in range(N - 1, -1, -1):  # range(start, end, increment)
        if heights[i] > max_height:
            answer += 1
            max_height = heights[i]

    return answer


result = solution(heights)
print(result)
