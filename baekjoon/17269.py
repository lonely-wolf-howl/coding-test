# 이름궁합 테스트

"""
예제 입력
8 14
LEESIYUN MIYAWAKISAKURA
"""

N, M = map(int, input().split())
A, B = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ''
min_len = min(N, M)

for i in range(min_len):
    AB += A[i] + B[i]

AB += A[min_len:] + B[min_len:]

arr = [alp[ord(i) - ord('A')] for i in AB]

# arr = []
# for i in AB:
#     index = ord(i) - ord('A')
#     value = alp[index]
#     arr.append(value)

for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        arr[j] += arr[j + 1]

print("{}%".format((arr[0] % 10) * 10 + (arr[1] % 10)))
