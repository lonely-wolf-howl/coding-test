# 강의실

"""
예제 입력
8
6 15 21
7 20 25
1 3 8
3 2 14
8 6 27
2 7 13
4 12 18
5 6 20
"""

import sys

input = sys.stdin.readline

import heapq

N = int(input())
lecs = []

for i in range(N):
    id, start, end = map(int, input().split())
    # [배정 전 강의 목록]에 삽입
    heapq.heappush(lecs, (start, end))

heap = []  # 강의실

# 1번째 강의가 끝나는 시간을 삽입
end = heapq.heappop(lecs)[1]
heapq.heappush(heap, end)

answer = 1  # 필요한 강의실의 최소 개수

for i in range(N - 1):
    # [배정 전 강의 목록]에서 '배정할 강의' 꺼내기
    temp_start, temp_end = heapq.heappop(lecs)
    # [배정 후 강의 목록]에서 '가장 일찍 끝나는' 강의 꺼내기
    end = heapq.heappop(heap)

    if temp_start < end:  # 강의 시간이 겹치면
        heapq.heappush(heap, end)  # '가장 일찍 끝나는 강의'는 기존 강의실에 다시 삽입
        heapq.heappush(heap, temp_end)  # 새로운 강의실에 '배정할 강의' 삽입
        answer += 1
    else:
        heapq.heappush(heap, temp_end)  # '배정할 강의'를 기존 강의실에 배정

print(answer)
