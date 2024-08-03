# 친구 네트워크

"""
예제 입력
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
"""

import sys

input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x, y = find(x), find(y)

    if x != y:
        parent[y] = x
        network[x] += network[y]

    print(network[x])


test_case = int(input())

for _ in range(test_case):
    F = int(input())
    friendships = [input().split() for _ in range(F)]

    parent, network = {}, {}

    for a, b in friendships:
        if a not in parent:
            parent[a] = a
            network[a] = 1
        if b not in parent:
            parent[b] = b
            network[b] = 1

        union(a, b)

"""
1. 친구 관계: Fred Barney

parent와 network에 Fred와 Barney를 추가합니다.

parent = {'Fred': 'Fred', 'Barney': 'Barney'}
network = {'Fred': 1, 'Barney': 1}

Union 연산:

find(Fred) = 'Fred' (Fred는 자신의 부모)
find(Barney) = 'Barney' (Barney는 자신의 부모)

Fred와 Barney는 서로 다른 집합에 있으므로, Barney를 Fred의 부모로 설정합니다.

parent = {'Fred': 'Fred', 'Barney': 'Fred'}
network = {'Fred': 2, 'Barney': 1}

출력: 2

2. 친구 관계: Barney Betty

parent와 network에 Betty를 추가합니다.

parent = {'Fred': 'Fred', 'Barney': 'Fred', 'Betty': 'Betty'}
network = {'Fred': 2, 'Barney': 1, 'Betty': 1}

Union 연산:

find(Barney) = 'Fred' (경로 압축 후 Barney의 부모는 Fred가 됩니다.)
find(Betty) = 'Betty' (Betty는 자신의 부모)

Barney와 Betty는 서로 다른 집합에 있으므로, Betty를 Fred의 부모로 설정합니다.

parent = {'Fred': 'Fred', 'Barney': 'Fred', 'Betty': 'Fred'}
network = {'Fred': 3, 'Barney': 1, 'Betty': 1}

출력: 3

3. 친구 관계: Betty Wilma

parent와 network에 Wilma를 추가합니다.

parent = {'Fred': 'Fred', 'Barney': 'Fred', 'Betty': 'Fred', 'Wilma': 'Wilma'}
network = {'Fred': 3, 'Barney': 1, 'Betty': 1, 'Wilma': 1}

Union 연산:

find(Betty) = 'Fred' (경로 압축 후 Betty의 부모는 Fred가 됩니다.)
find(Wilma) = 'Wilma' (Wilma는 자신의 부모)

Betty와 Wilma는 서로 다른 집합에 있으므로, Wilma를 Fred의 부모로 설정합니다.

parent = {'Fred': 'Fred', 'Barney': 'Fred', 'Betty': 'Fred', 'Wilma': 'Fred'}
network = {'Fred': 4, 'Barney': 1, 'Betty': 1, 'Wilma': 1}

출력: 4
"""
