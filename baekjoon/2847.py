# https://www.acmicpc.net/problem/2847

n = int(input())

points = []

for _ in range(n):
    points.append(int(input()))

count = 0

# for index in range(start, stop, step)
for i in range(n - 2, -1, -1):
    if points[i] >= points[i + 1]:
        count += points[i] - (points[i + 1] - 1)
        points[i] = points[i + 1] - 1

print(count)
