# https://www.acmicpc.net/problem/1068

import sys

n = int(input().strip())
parent = list(map(int, input().split()))
remove_node = int(input().strip())

# find root and build children list
children = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parent[i] == -1:
        root = i
        continue
    if i == remove_node:
        continue
    if parent[i] == remove_node:
        continue
    children[parent[i]].append(i)

# children
# [[1], [3, 4], [], [], []]

if remove_node == root:
    print(0)
    sys.exit(0)

stack = [root]
leaf_count = 0

while stack:
    node: int = stack.pop()

    if not children[node]:  # if the current node has no children
        leaf_count += 1
    else:
        stack.extend(children[node])  # visit its children

print(leaf_count)
