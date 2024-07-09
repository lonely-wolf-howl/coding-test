# 소수의 곱

"""
예제 입력
4 19
2 3 5 7
"""

import sys
import heapq

input = sys.stdin.readline

# 소수의 개수 K와 출력할 N번째 수
K, N = map(int, input().split())
data = list(map(int, input().split()))

heap = []
visited = set()  # 이미 처리된 수
max_value = max(data)

for x in data:  # 초기 원소 삽입
    heapq.heappush(heap, x)

# N-1개의 원소 꺼내기
for i in range(N - 1):
    element = heapq.heappop(heap)
    for x in data:
        temp = element * x  # 곱한 결과 계산
        if len(heap) >= N and max_value < temp:
            continue
        if temp not in visited:  # 처음 방문하는 수라면
            heapq.heappush(heap, temp)
            max_value = max(max_value, temp)
            visited.add(temp)  # 방문 처리

# N번째 원소 꺼내기
print(heapq.heappop(heap))

"""
* 초기 상태
heap: [2, 3, 5, 7]
visited: {}

* 1단계
element: 2 (heap에서 추출)

곱셈 결과:
2 * 2 = 4 (temp)
2 * 3 = 6
2 * 5 = 10
2 * 7 = 14

heap: [3, 4, 5, 7, 6, 10, 14]
visited: {4, 6, 10, 14}

* 2단계
element: 3 (heap에서 추출)

곱셈 결과:
3 * 2 = 6 (이미 visited에 있음, 무시)
3 * 3 = 9
3 * 5 = 15
3 * 7 = 21

heap: [4, 5, 7, 6, 10, 14, 9, 15, 21]
visited: {4, 6, 9, 10, 14, 15, 21}
"""
