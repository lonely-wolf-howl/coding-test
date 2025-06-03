# 저울
# https://www.acmicpc.net/problem/2437

N = int(input())
weights = list(map(int, input().split()))

weights.sort()
target = 1  # smallest weight that cannot be measured yet

for w in weights:
    if w > target:
        break
    target += w

    # w=1 → target=2
    # w=1 → target=3
    # w=2 → target=5

print(target)
