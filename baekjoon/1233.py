# 주사위
# https://www.acmicpc.net/problem/1233


"""
예제 입력
3 2 3
"""

S1, S2, S3 = map(int, input().split())
counter = dict()

# 3중 반복문을 이용해 모든 경우의 수 계산 (완전 탐색)
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            sum: int = i + j + k  # 눈금의 합 게산
            # 눈금의 합 등장 횟수 세기
            if sum not in counter:
                counter[sum] = 1
            else:
                counter[sum] += 1

# 가장 많이 등장한 눈금의 합 찾기
max_count = -1
answer = int(1e9)

for key, value in counter.items():
    # 등장 횟수가 더 많은 눈금의 합을 찾은 경우
    if max_count < value:
        max_count = value
        answer = key
    elif max_count == value:
        # 답이 여러 개라면, 가장 합이 작은 것으로 대체
        answer = min(answer, key)

print(answer)
