# 풍선 터뜨리기

"""
예제 입력
5
3 2 1 -3 -1

예제 출력
1 4 5 3 2
"""

import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
ARR = list(map(int, input().split()))

deq = deque()

for i in range(N):
    # (종이에 적혀 있는 수, 풍선 번호) 형태로 원소를 삽입
    deq.append((ARR[i], i + 1))

result = []

paper_num, balloon_num = deq.popleft()  # 1번째 원소 추출
result.append(balloon_num)

for i in range(N - 1):  # 원소를 모두 꺼내기
    if paper_num > 0:
        for j in range(paper_num - 1):
            deq.append(deq.popleft())  # 시계 방향 회전
    else:
        for j in range(-paper_num):
            deq.appendleft(deq.pop())  # 반시계 방향 회전

    paper_num, balloon_num = deq.popleft()  # 원소 추출
    result.append(balloon_num)

for x in result:
    print(x, end=" ")

"""
(3, 1)(2, 2)(1, 3)(-3, 4)(-1, 5)
      (2, 2)(1, 3)(-3, 4)(-1, 5) -> 1

시계 방향 회전 2번

(-3, 4)(-1, 5)(2, 2)(1, 3)
       (-1, 5)(2, 2)(1, 3) -> 4

반시계 방향 회전 3번

(-1, 5)(2, 2)(1, 3)   
       (2, 2)(1, 3) -> 5

반시계 방향 회전 1번

(1, 3)(2, 2)
      (2, 2) -> 3
"""
