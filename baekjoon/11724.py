# 연결 요소의 개수

import sys

input = sys.stdin.readline


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 점의 개수 N과 간선의 개수 M
N, M = map(int, input().split())

parent = [0] * (N + 1)

# 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i

for i in range(M):  # M은 합치기(union) 연산의 수와 동일
    a, b = map(int, input().split())
    union_parent(parent, a, b)

counter = set()  # 고유한 집합의 수

for i in range(1, N + 1):
    counter.add(find_parent(parent, i))

print(len(counter))
