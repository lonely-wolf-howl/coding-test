# 행복

"""
예제 입력
5
27 35 92 75 42
"""

# 내 풀이
N = input()
scores = list(map(int, input().split()))

max = -1
min = 10000

for i in range(len(scores)):
    if scores[i] > max:
        max = scores[i]
    if scores[i] < min:
        min = scores[i]

result = max - min
print(result)

# 해설
N, scores = input(), list(map(int, input().split()))

print(max(scores) - min(scores))
