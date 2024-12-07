# 수빈이와 수열

"""
예제 입력
4
3 2 3 5
"""

# 내 풀이
N = input()
B = list(map(int, input().split()))

A = []

for i in range(len(B)):
    temp = ((i + 1) * B[i]) - (i * B[i - 1])
    A.append(temp)

print(*A)

# 해설
N, B = int(input()), list(map(int, input().split()))

A = [0 for i in range(len(B))]
A[0] = B[0]

for i in range(1, N):
    A[i] = ((i + 1) * B[i] - sum(A))

for i in A:
    print(i, end=' ')
