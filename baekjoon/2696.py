# 중앙값 구하기

"""
예제 입력
1
9
1 2 3 4 5 6 7 8 9
"""

import sys
import heapq

input = sys.stdin.readline


def show_result():
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=" ")
        if (i + 1) % 10 == 0:  # 10개 단위로 줄바꿈
            print()
    print()


T = int(input())
for _ in range(T):
    M = int(input())

    data = []
    for _ in range(M // 10 + 1):
        data.extend(list(map(int, input().split())))  # 수열 입력

    left = []  # 왼쪽 Max Heap (중앙값 이하의 값들을 저장)
    right = []  # 오른쪽 Min Heap (중앙값 이상의 값들을 저장)
    middle = data[0]  # 첫 번째 원소를 중앙값으로 설정

    result = [middle]  # 결과 배열 초기화 및 첫 번째 중앙값 추가

    for i in range(1, M):  # 입력받은 수열의 원소를 하나씩 확인
        if data[i] <= middle:
            heapq.heappush(left, -data[i])  # 중앙값 이하의 값은 왼쪽에 추가
        else:
            heapq.heappush(right, data[i])  # 중앙값 이상의 값은 오른쪽에 추가

        # 홀수 번째 수를 읽을 차례이면 중앙값을 갱신
        if i % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, middle)  # 현재 중앙값을 오른쪽에 추가
                middle = -heapq.heappop(left)  # 왼쪽 최대값을 중앙값으로 설정
            elif len(left) < len(right):
                heapq.heappush(left, -middle)  # 현재 중앙값을 왼쪽에 추가
                middle = heapq.heappop(right)  # 오른쪽 최소값을 중앙값으로 설정
            result.append(middle)  # 갱신된 중앙값을 결과 배열에 추가

    show_result()
