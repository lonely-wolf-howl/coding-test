# 소수의 곱
# https://www.acmicpc.net/problem/2014

"""
예제 입력
4 19
2 3 5 7
"""

import heapq


K, N = map(int, input().split())
data = list(map(int, input().split()))

heap = []
visited = set()
max_value = max(data)

for x in data:
    heapq.heappush(heap, x)

for i in range(N - 1):
    element = heapq.heappop(heap)
    for x in data:
        temp = element * x
        if len(heap) >= N and max_value < temp:
            continue
        if temp not in visited:
            heapq.heappush(heap, temp)
            max_value = max(max_value, temp)
            visited.add(temp)

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
