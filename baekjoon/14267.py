# https://www.acmicpc.net/problem/14267

from collections import deque

n, m = map(int, input().split())
parent = list(map(int, input().split()))

for i in range(1, n):
    parent[i] -= 1

# parent
# [-1, 0, 1, 2, 3]

praise = [0] * n
for _ in range(m):
    employee, weight = map(int, input().split())
    praise[employee - 1] += weight

# praise
# [0, 2, 4, 0, 6]

# find root and build children list
children = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        children[parent[i]].append(i)

# children
# [[1], [2], [3], [4], []]

total = praise[:]  # direct praise each employee received
total[root] = 0

queue = deque([root])
while queue:
    node = queue.popleft()  # # current employee

    for child in children[node]:
        total[child] += total[node]  # pass down accumulated praise
        queue.append(child)

print(*total)
