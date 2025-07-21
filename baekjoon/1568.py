# https://www.acmicpc.net/problem/1568

N = int(input())

K = 1
sec = 0

while N != 0:
    if K > N:
        K = 1
    N -= K
    K += 1
    sec += 1

print(sec)
