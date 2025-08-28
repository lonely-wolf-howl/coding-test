# https://www.acmicpc.net/problem/11720

n = int(input())
s = str(input())

sum = 0

for i in range(n):
    sum += ord(s[i]) - ord("0")

print(sum)
