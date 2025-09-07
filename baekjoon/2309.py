# https://www.acmicpc.net/problem/2309

from itertools import combinations

heights = []

for _ in range(9):
    height = int(input())
    heights.append(height)

for selected in combinations(heights, 7):
    if sum(selected) == 100:
        valid = list(selected)
        valid.sort()
        for height in valid:
            print(height)
        break
