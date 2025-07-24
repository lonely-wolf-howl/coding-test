# https://www.acmicpc.net/problem/1668


def asc(arr):
    current: int = arr[0]
    result = 1
    for i in range(1, len(arr)):
        if current < arr[i]:
            result += 1
            current = arr[i]
    return result


N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

print(asc(arr))
arr.reverse()
print(asc(arr))
