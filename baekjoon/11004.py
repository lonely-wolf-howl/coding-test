# https://www.acmicpc.net/problem/11004

"""
예제 입력
5 2
4 1 2 3 5
"""

N, K = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

new_arr = sorted(arr)

print(new_arr[K - 1])
