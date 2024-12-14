# The candy war
# https://www.acmicpc.net/problem/9037

"""
예제 입력
4
5
2 4 7 8 9
1
9
6
10 5 13 2 7 8
4
3 4 4 3
"""

from typing import List


def is_all_equal(C: List[int]) -> bool:
    if len(set(C)) == 1:
        return True
    else:
        return False


def make_all_even(C: List[int]) -> None:
    for i in range(len(C)):
        if C[i] % 2 == 1:
            C[i] += 1
        else:
            continue


def distribute_and_merge(N: int, C: List[int]) -> None:
    arr: List[int] = [0 for _ in range(N)]

    for i in range(N):
        arr[(i + 1) % N] = C[i] // 2  # modulo operation
        C[i] = C[i] // 2

    for i in range(N):
        C[i] += arr[i]


def process() -> None:
    N = int(input())
    C = list(map(int, input().split()))

    count: int = 0

    make_all_even(C)

    while not is_all_equal(C):
        count += 1
        distribute_and_merge(N, C)
        make_all_even(C)

    print(count)


T = int(input())

for i in range(T):
    process()
