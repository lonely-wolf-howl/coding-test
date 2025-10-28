# https://www.acmicpc.net/problem/2217

n = int(input())

ropes = [0] * n
for i in range(n):
    ropes[i] = int(input())

# desc
ropes.sort(reverse=True)

max_load = 0
for i in range(n):
    current_load = ropes[i] * (i + 1)
    if current_load > max_load:
        max_load = current_load

print(max_load)
