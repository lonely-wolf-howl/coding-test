# 절댓값 힙

import sys

input = sys.stdin.readline

import heapq

N = int(input())

# 초기화
heap = []

for i in range(N):
    x = int(input())

    # 삭제 연산일 경우
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            absolute, original = heapq.heappop(heap)
            print(original)
    # 삽입 연산일 경우
    else:
        heapq.heappush(heap, (abs(x), x))
