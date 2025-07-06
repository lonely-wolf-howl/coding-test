# https://www.acmicpc.net/problem/11650

N = int(input())
arr = []

for i in range(N):
    data = input().split(" ")
    arr.append((int(data[0]), int(data[1])))

new_arr = sorted(arr, key=lambda x: (x[0], x[1]))

for i in new_arr:
    print(i[0], i[1])
