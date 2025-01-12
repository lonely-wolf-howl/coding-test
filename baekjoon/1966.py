# 프린터 큐
# https://www.acmicpc.net/problem/1966

"""
예제 입력
1
6 0
1 1 9 1 1 1
"""

from collections import deque

test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    indexed_queue = []
    for index, priority in enumerate(queue):
        indexed_queue.append((priority, index))
    queue = deque(indexed_queue)

    count = 0

    while queue:
        current_document = queue.popleft()

        has_higher_priority = False
        for document in queue:
            # 현재 문서의 우선순위보다 높은 문서가 있을 경우
            if current_document[0] < document[0]:
                has_higher_priority = True
                break

        if has_higher_priority:
            queue.append(current_document)
        else:
            count += 1
            if current_document[1] == M:
                print(count)
                break
