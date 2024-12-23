# 두 개의 손
# https://www.acmicpc.net/problem/16675

"""
예제 입력
R S P R
"""

ML, MR, TL, TR = ('RSP'.index(i) for i in input().split())

# print(ML, MR, TL, TR)
# 0 1 2 0

if ML == MR and (ML + 2) % 3 in [TL, TR]:
    print("TK")
elif TL == TR and (TL + 2) % 3 in [ML, MR]:
    print("MS")
else:
    print("?")
