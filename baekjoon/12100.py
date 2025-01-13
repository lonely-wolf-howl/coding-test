# 2048 (easy)
# https://www.acmicpc.net/problem/12100

"""
예제 입력
3
2 2 2
4 4 4
8 8 8
"""

from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_block = 0


def left(board):
    for i in range(N):
        cursor: int = 0
        for j in range(1, N):
            if board[i][j] != 0:
                temp: int = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = temp
                elif board[i][cursor] == temp:
                    board[i][cursor] *= 2
                    cursor += 1
                else:
                    cursor += 1  # pass
                    board[i][cursor] = temp

    return board


def right(board):
    for i in range(N):
        cursor: int = N - 1
        for j in range(N - 1, -1, -1):

            if board[i][j] != 0:
                temp: int = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = temp
                elif board[i][cursor] == temp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = temp
    return board


def up(board):
    for j in range(N):
        cursor: int = 0
        for i in range(N):
            if board[i][j] != 0:
                temp: int = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = temp
                elif board[cursor][j] == temp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = temp
    return board


def down(board):
    for j in range(N):
        cursor: int = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                temp: int = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = temp
                elif board[cursor][j] == temp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = temp
    return board


def dfs(n: int, board):
    global max_block

    if n == 5:
        for i in range(N):
            for j in range(N):
                if board[i][j] > max_block:
                    max_block = board[i][j]
        return

    for i in range(4):
        board_copy = deepcopy(board)

        if i == 0:
            dfs(n + 1, left(board_copy))
        elif i == 1:
            dfs(n + 1, right(board_copy))
        elif i == 2:
            dfs(n + 1, up(board_copy))
        else:
            dfs(n + 1, down(board_copy))


dfs(0, board)

print(max_block)
