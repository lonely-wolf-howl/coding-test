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

print(left)
