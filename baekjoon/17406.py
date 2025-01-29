# 배열 돌리기 4
# https://www.acmicpc.net/problem/17406

"""
예제 입력
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
"""

import copy


def rotate(matrix, r, c, s):
    r -= 1
    c -= 1
    for layer in range(1, s + 1):
        top = r - layer
        bottom = r + layer
        left = c - layer
        right = c + layer

        temp = matrix[top][right]

        # top side (left to right)
        for i in range(right, left, -1):
            matrix[top][i] = matrix[top][i - 1]

        # left side (bottom to top)
        for i in range(top, bottom):
            matrix[i][left] = matrix[i + 1][left]

        # bottom side (right to left)
        for i in range(left, right):
            matrix[bottom][i] = matrix[bottom][i + 1]

        # right side (top to bottom)
        for i in range(bottom, top, -1):
            matrix[i][right] = matrix[i - 1][right]

        matrix[top + 1][right] = temp


def calculate_min_value(matrix):
    return min([sum(row) for row in matrix])


def dfs(matrix, operations, used, depth, min_result):
    if depth == len(operations):
        return min(min_result, calculate_min_value(matrix))

    for i, (r, c, s) in enumerate(operations):
        if not used[i]:
            used[i] = True
            new_matrix = copy.deepcopy(matrix)
            rotate(new_matrix, r, c, s)
            min_result = min(
                min_result, dfs(new_matrix, operations, used, depth + 1, min_result)
            )
            used[i] = False

    return min_result


def solve(N, M, K, A, Q):
    min_result = float("inf")
    used = [False] * K
    min_result = dfs(A, Q, used, 0, min_result)
    print(min_result)


if __name__ == "__main__":
    N, M, K = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]
    Q = [list(map(int, input().split())) for _ in range(K)]

    solve(N, M, K, A, Q)
