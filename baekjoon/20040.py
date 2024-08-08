# 사이클 게임

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


# 점의 개수 n과 차례의 수 m
n, m = map(int, input().split())

parent = [0] * n

for i in range(n):
    parent[i] = i

cycle = False

for i in range(m):  # m은 합치기(union) 연산의 수와 동일
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print(i + 1)
        break
    else:
        union_parent(parent, a, b)

if not cycle:
    print(0)

"""
* 1단계: 입력 '0 1'

1. find_parent(parent, 0) 호출
  parent[0] == 0이므로 0 반환
2. find_parent(parent, 1) 호출
  parent[1] == 1이므로 1 반환
3. 두 집합을 합치기
  union_parent(parent, 0, 1)
  parent[1] = 0

parent = [0, 0, 2, 3, 4, 5]

* 2단계: 입력 '1 2'

1. find_parent(parent, 1) 호출
  parent[1] == 0이므로 find_parent(parent, 0) 호출
  parent[0] == 0이므로 0 반환
2. find_parent(parent, 2) 호출
  parent[2] == 2이므로 2 반환
3. 두 집합을 합치기
  union_parent(parent, 1, 2)
  parent[2] = 0

parent = [0, 0, 0, 3, 4, 5]

* 3단계: 입력 '1 3'

1. find_parent(parent, 1) 호출
  parent[1] == 0이므로 find_parent(parent, 0) 호출
  parent[0] == 0이므로 0 반환
2. find_parent(parent, 3) 호출
  parent[3] == 3이므로 3 반환
3. 두 집합을 합치기
  union_parent(parent, 1, 3)
  parent[3] = 0

parent = [0, 0, 0, 0, 4, 5]

* 4단계: 입력 '0 3'

1. find_parent(parent, 0) 호출
  parent[0] == 0이므로 0 반환
2. find_parent(parent, 3) 호출
  parent[3] == 0이므로 find_parent(parent, 0) 호출
  parent[0] == 0이므로 0 반환
3. find_parent 결과가 같으므로 종료
"""
