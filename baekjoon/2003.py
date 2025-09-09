# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0

sum = a[0]
count = 0

while True:
    if sum == m:
        count += 1
    if sum >= m:
        start += 1
        sum -= a[start - 1]
    else:
        if end == n - 1:
            break
        end += 1
        sum += a[end]

print(count)
