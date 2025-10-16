# https://www.acmicpc.net/problem/2417

n = int(input())

left = 0
right = n

while left < right:
    mid = (left + right) // 2

    if mid * mid >= n:
        right = mid
    else:
        left = mid + 1

"""
left  right  mid  mid²  comparison
   0     16    8   64      64 ≥ 16
   0      8    4   16      16 ≥ 16
   0      4    2    4       4 < 16
   3      4    3    9       9 < 16
"""

print(left)
