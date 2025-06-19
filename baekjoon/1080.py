# 행렬
# https://www.acmicpc.net/problem/1080


def flip(matrix, x, y):
    for i in range(3):
        for j in range(3):
            if matrix[x + i][y + j] == 0:
                matrix[x + i][y + j] = 1
            else:
                matrix[x + i][y + j] = 0


def main():
    N, M = map(int, input().split())
    A = [list(map(int, list(input().strip()))) for _ in range(N)]
    B = [list(map(int, list(input().strip()))) for _ in range(N)]

    count = 0

    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                count += 1

    if A == B:
        print(count)
    else:
        print(-1)


if __name__ == "__main__":
    main()
