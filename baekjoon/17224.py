# APC는 왜 서브태스크 대회가 되었을까?
# https://www.acmicpc.net/problem/17224

"""
예제 입력
4 8 4
1 8
4 5
6 20
9 12
"""

N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())

    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# X, O
# X, O
# O, X
# X, X

# hard = 2
# easy = 1

answer = min(hard, K) * 140

if hard < K:
    answer += min(easy, K - hard) * 100

print(answer)
