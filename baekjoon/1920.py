# 수 찾기

"""
예제 입력
5
4 1 5 2 3
5
1 3 7 9 5
"""

# 풀이 1
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for x in B:
    if x not in A:
        print("0")
    else:
        print("1")

# 풀이 2
N = int(input()),
A = {i: 1 for i in map(int, input().split())}
M = int(input()),
B = list(map(int, input().split()))

# print(A)
# {4: 1, 1: 1, 5: 1, 2: 1, 3: 1}

for i in B:
    print(A.get(i, 0))
