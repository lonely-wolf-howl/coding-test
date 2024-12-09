# 보너스 점수

"""
예제 입력
8
XOOOXOOX
"""

# 내 풀이
N, S = int(input()), input()

score = []
bonus = 0

for i in range(N):
    if S[i] == "O":
        score.append(i + 1)
        score.append(bonus)
        bonus += 1
    else:
        bonus = 0

print(sum(score))

# 해설
N, S = input(), input()

score, bonus = 0, 0

for index, value in enumerate(S):
    if value == "O":
        score += index + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)
