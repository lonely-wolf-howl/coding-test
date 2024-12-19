# 주사위 세개
# https://www.acmicpc.net/problem/2480

"""
예제 입력
3 3 6
"""

dice_list = list(map(int, input().split()))

dice_list.sort()

if len(set(dice_list)) == 1:
    print(10000 + dice_list[0] * 1000)
elif len(set(dice_list)) == 2:
    print(1000 + dice_list[1] * 100)
else:
    print(dice_list[2] * 100)
