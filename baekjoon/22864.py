# https://www.acmicpc.net/problem/22864

a, b, c, m = map(int, input().split())

fatigue = 0
work = 0

for i in range(24):
    if fatigue + a <= m:
        fatigue += a
        work += b
    else:
        fatigue -= c  # take a rest
        fatigue = max(0, fatigue)

print(work)
