# https://www.acmicpc.net/problem/2747

n = int(input())

a = 0
b = 1

while n > 0:
    temp: int = a
    a = b
    b = temp + b
    n -= 1

print(a)
