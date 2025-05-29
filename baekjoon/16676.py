# 근우의 다이어리 꾸미기
# https://www.acmicpc.net/problem/16676

N = input()
S: str = "1" * len(N)

if len(N) == 1:
    print(1)
elif int(N) >= int(S):
    print(len(N))  # N = 111, S = "111" → need 3 sticker packs
else:
    print(len(N) - 1)  # N = 110, S = "111" → need 2 sticker packs
