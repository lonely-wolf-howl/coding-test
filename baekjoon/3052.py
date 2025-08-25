# https://www.acmicpc.net/problem/3052

check = [0] * 42

for i in range(10):
    n = int(input())
    check[n % 42] = 1

sum = 0

for i in range(42):
    sum += check[i]

print(sum)
