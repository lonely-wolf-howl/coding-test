# 대칭 차집합
# https://www.acmicpc.net/problem/1269

"""
예제 입력
3 5
1 2 4
2 3 4 5 6
"""


def process(a_list, b_list):
    a_list.sort()  # time complexity: n log n
    b_list.sort()

    i = j = 0
    count = 0

    while i < len(a_list) and j < len(b_list):
        if a_list[i] < b_list[j]:
            count += 1
            i += 1
        elif a_list[i] > b_list[j]:
            count += 1
            j += 1
        else:
            i += 1
            j += 1

    count += (len(a_list) - i) + (len(b_list) - j)

    return count


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(process(a, b))
