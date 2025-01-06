# 강의실
# https://www.acmicpc.net/problem/1374

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


import heapq

N = int(input())
lecs = []

for i in range(N):
    num, start, end = map(int, input().split())
    # [배정 전 강의 목록]에 삽입
    heapq.heappush(lecs, (start, end))

# 각 강의실에서 진행 중인 강의의 종료 시간을 저장
classroom_end_times = []

# 1번째 강의가 끝나는 시간을 삽입
end: int = heapq.heappop(lecs)[1]
heapq.heappush(classroom_end_times, end)

# 필요한 강의실의 최소 개수
answer = 1

for i in range(N - 1):
    # [배정 전 강의 목록]에서 '배정할 강의' 꺼내기
    temp_start, temp_end = heapq.heappop(lecs)
    # [배정 후 강의 목록]에서 '가장 일찍 끝나는' 강의 꺼내기
    earliest_end_time: int = heapq.heappop(classroom_end_times)

    if temp_start < earliest_end_time:
        # '가장 일찍 끝나는 강의'는 기존 강의실에 다시 삽입
        heapq.heappush(classroom_end_times, earliest_end_time)
        # 새로운 강의실에 '배정할 강의' 삽입
        heapq.heappush(classroom_end_times, temp_end)
        answer += 1
    else:
        # '배정할 강의'를 기존 강의실에 배정
        heapq.heappush(classroom_end_times, temp_end)

print(answer)
