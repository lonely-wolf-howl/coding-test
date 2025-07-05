# https://www.acmicpc.net/problem/10814

N = int(input())
arr = []

for i in range(N):
    data = input().split(" ")
    arr.append((int(data[0]), data[1]))
    # each element is a tuple: (int, str)
    # tuples are immutable sequences, and they can be used as sort keys

new_arr = sorted(arr, key=lambda x: x[0])
# 'sorted()' returns a new list and does not modify the original
# python's sort is stable, so original order is preserved when ages are equaL

for i in new_arr:
    print(i[0], i[1])
