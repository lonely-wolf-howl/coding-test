# https://www.acmicpc.net/problem/1920

a = set(map(int, input().split()))
b = list(map(int, input().split()))

for x in b:
    if x not in a:
        print("0")
    else:
        print("1")
