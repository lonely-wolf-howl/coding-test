# 이중 우선순위 큐

"""
예제 입력
1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
"""

import sys
import heapq

input = sys.stdin.readline

T = int(input())  # 1

for i in range(T):
    k = int(input())  # 9

    min_heap, max_heap = [], []

    deleted = [True] * (k + 1)  # 삭제 여부를 추적

    for i in range(k):
        operator, number = input().split()  # 연산과 숫자 입력
        number = int(number)

        if operator == "I":  # 삽입 연산
            heapq.heappush(min_heap, (number, i))
            heapq.heappush(max_heap, (-number, i))
            deleted[i] = False
        elif operator == "D":  # 삭제 연산
            if number == -1:  # 최솟값 삭제
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
            elif number == 1:  # 최댓값 삭제
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)

        # 유효하지 않은 요소를 제거
        while min_heap and deleted[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and deleted[max_heap[0][1]]:
            heapq.heappop(max_heap)

    # 결과 출력
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")


# 예시
min_heap = [(7, 0), (5, 1), (3, 2)]
heapq.heapify(min_heap)
#     3 (2)
#    /     \
# 5 (1)   7 (0)
deleted = [False, False, False]  # 초기 상태: 모든 요소가 유효함

print(min_heap)  # [(3, 2), (5, 1), (7, 0)]

# 최솟값
if min_heap:
    deleted[min_heap[0][1]] = True
    heapq.heappop(min_heap)  # 최솟값 삭제

print(deleted)  # [False, True, False]
print(min_heap)  # [(5, 1), (7, 0)]

# 실제 값: 7, 5, 3
max_heap = [(-7, 0), (-5, 1), (-3, 2)]  # 음수로 변환
heapq.heapify(max_heap)
#     -7 (0)
#    /     \
# -5 (1)  -3 (2)
deleted = [False, False, False]  # 초기 상태: 모든 요소가 유효함

print(max_heap)  # [(-7, 0), (-5, 1), (-3, 2)]

# 최댓값 삭제
if max_heap:
    deleted[max_heap[0][1]] = True
    heapq.heappop(max_heap)  # 최댓값 삭제

print(deleted)  # [True, False, False]
print(max_heap)  # [(-5, 1), (-3, 2)]
