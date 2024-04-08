# 나는 요리사다

"""
예제입력
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5
"""

import sys

input = sys.stdin.readline

result = 0  # 최종 우승자
max_value = 0  # 평가 점수의 최댓값

# i = 0, 1, 2, 3, 4
for i in range(5):
    row = list(map(int, input().split()))

    summary = sum(row)  # 현재 요리사의 평가 점수 합
    if max_value < summary:
        max_value = summary
        result = i + 1

print(result, max_value)
