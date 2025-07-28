# https://www.acmicpc.net/problem/2250


class Node:
    def __init__(self, id, left_node, right_node):
        self.parent = -1
        self.id = id
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, level):
    global column, level_depth

    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)

    level_min[level] = min(level_min[level], column)
    level_max[level] = max(level_max[level], column)
    column += 1

    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


n = int(input())

tree = {}
level_min = [n]
level_max = [0]
root = -1
column = 1
level_depth = 1

for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    id, left_node, right_node = map(int, input().split())
    tree[id].left_node = left_node
    tree[id].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = id
    if right_node != -1:
        tree[right_node].parent = id

for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)
