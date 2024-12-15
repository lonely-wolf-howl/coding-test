# Mixing Milk
# https://www.acmicpc.net/problem/16769

"""
예제 입력
10 3
11 4
12 5
"""

C = []
M = []

for _ in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

N: int = 100

for i in range(N):
    idx: int = i % 3
    next_idx: int = (idx + 1) % 3

    # M[idx]: 현재 통에서 이동할 수 있는 우유의 양
    # C[next_idx] - M[next_idx]: 다음 통이 받을 수 있는 우유의 양
    transfer_amount: int = min(M[idx], C[next_idx] - M[next_idx])

    M[idx] -= transfer_amount
    M[next_idx] += transfer_amount

for i in M:
    print(i)
