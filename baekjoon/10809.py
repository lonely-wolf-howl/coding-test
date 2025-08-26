# https://www.acmicpc.net/problem/10809

s = input()

check = [-1] * 26

for i in range(len(s)):
    index = ord(s[i]) - ord("a")

    if check[index] == -1:
        check[index] = i

for i in range(26):
    print(check[i], end=" ")
