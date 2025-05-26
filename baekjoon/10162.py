# 전자레인지
# https://www.acmicpc.net/problem/10162


def solve():
    T = int(input())

    # // : integer division operator
    # % : modulo operator

    if T % 10 != 0:
        print(-1)
        return

    a = T // 300  # 100 // 300 = 0
    T %= 300  # 100 % 300 = 100

    b = T // 60  # 100 // 60 = 1
    T %= 60  # 100 % 60 = 40

    c = T // 10  # 40 // 10 = 4

    print(a, b, c)


if __name__ == "__main__":
    solve()
