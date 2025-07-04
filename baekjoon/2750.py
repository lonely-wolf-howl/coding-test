# 수 정렬하기
# https://www.acmicpc.net/problem/2750

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)
