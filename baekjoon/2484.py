# 주사위 네개
# https://www.acmicpc.net/problem/2484

"""
예제 입력
4
3 3 3 3
3 3 6 3
2 2 6 6
6 2 1 5
"""

from typing import List


def process(dice_list: List[int]) -> int:
    dice_list.sort()

    if len(set(dice_list)) == 1:
        return 50000 + dice_list[0] * 5000
    elif len(set(dice_list)) == 2:
        if dice_list[1] == dice_list[2]:
            return 10000 + dice_list[1] * 1000
        else:
            return 2000 + (dice_list[1] + dice_list[2]) * 500
    elif len(set(dice_list)) == 3:
        for i in range(3):
            if dice_list[i] == dice_list[i + 1]:
                return 1000 + dice_list[i] * 100
    else:
        return dice_list[-1] * 100


N: int = int(input())
results: List[int] = []

for _ in range(N):
    dice_list: List[int] = list(map(int, input().split()))
    results.append(process(dice_list))

print(max(results))
