# Z
# https://www.acmicpc.net/problem/1074

"""
예제 입력
2 3 1
"""

N, r, c = map(int, input().split())


def Z(size: int, x: int, y: int) -> int:
    if size == 1:
        return 0

    size //= 2

    if x < size and y < size:
        return 0 * size * size + Z(size, x, y)
    elif x < size and y >= size:
        return 1 * size * size + Z(size, x, y - size)
    elif x >= size and y < size:
        return 2 * size * size + Z(size, x - size, y)
    else:
        return 3 * size * size + Z(size, x - size, y - size)


print(Z(2 ** N, r, c))
