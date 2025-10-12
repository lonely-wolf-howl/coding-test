# https://www.acmicpc.net/problem/1748


def process(n: int) -> int:
    if n <= 0:
        return 0

    digits = 1
    start, end = 1, 9

    total = 0

    # 1 ~ 9, 10 ~ 99, 100 ~ 999
    while n >= start:
        upper = n if n < end else end

        # += (count of integers in this range) * digits
        total += (upper - start + 1) * digits

        # move to next digit range
        digits = digits + 1
        start, end = start * 10, end * 10 + 9

    return total


if __name__ == "__main__":
    n = int(input())
    print(process(n))
