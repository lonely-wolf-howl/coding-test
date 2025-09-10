# https://www.acmicpc.net/problem/7795

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    j = 0
    ans = 0

    for i in range(n):
        while j < m and a[i] > b[j]:
            j += 1
        ans += j

    print(ans)
