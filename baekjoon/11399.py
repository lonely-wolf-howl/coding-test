# https://www.acmicpc.net/problem/11399

n = int(input())
times = list(map(int, input().split()))

times.sort()

running = 0
total_wait = 0

for t in times:
    running += t
    total_wait += running

print(total_wait)
