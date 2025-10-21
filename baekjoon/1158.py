# https://www.acmicpc.net/problem/1158

from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n + 1))
answer = []

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())  # rotate
    answer.append(queue.popleft())

text = ", ".join(map(str, answer))
print(f"<{text}>")
