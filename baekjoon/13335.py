# 트럭

"""
예제 입력
4 2 10
7 4 5 6
"""

import sys
from collections import deque

input = sys.stdin.readline

# 입력
n, w, L = map(int, input().split())  # n: 자동차 수, w: 다리의 길이, L: 다리의 최대 하중
trucks = deque(map(int, input().split()))  # 자동차들의 무게 목록

# 초기화
bridge = deque()  # 다리의 상태 (현재 다리 위에 있는 자동차들을 나타냄)
total_weight = 0  # 현재 다리 위에 있는 자동차들의 무게 합
time = 0  # 총 소요 시간

# 실행
while True:
    # 모든 자동차가 다리를 건넜고, 다리 위에 자동차가 없을 때 종료
    if len(trucks) == 0 and total_weight == 0:
        break

    # 다리 길이만큼 자동차가 올라와 있을 때, 가장 앞의 자동차를 제거
    if len(bridge) == w:
        exiting_car = bridge.popleft()
        total_weight -= exiting_car

    # 다음 자동차가 다리에 진입할 수 있는지 확인
    if len(trucks) > 0 and total_weight + trucks[0] <= L:
        bridge.append(trucks[0])
        total_weight += trucks[0]
        trucks.popleft()
    else:
        # 자동차가 다리에 진입하지 못하고 대기해야 하는 경우
        bridge.append(0)  # 다리의 상태를 유지하기 위해 0을 추가

    time += 1  # 시간 증가

print(time)  # 총 소요 시간 출력
