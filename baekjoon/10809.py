# 알파벳 찾기

import sys

input = sys.stdin.readline

ARRAY = [-1] * 26
S = input().strip()  # 문자열 입력

for i in range(len(S)):  # 문자를 하나씩 확인
    index = ord(S[i]) - ord("a")
    if ARRAY[index] == -1:  # 처음 등장했다면
        ARRAY[index] = i  # 배열에 등장한 위치 기록

for result in ARRAY:
    print(result, end=" ")
