# 본대 산책
# https://www.acmicpc.net/problem/12849

# 0: 정보과학관
# 1: 전산관
# 2: 미래관
# 3: 신앙관
# 4: 한경직기념관
# 5: 진리관
# 6: 형남공학관
# 7: 학생회관

# 0분에 특정 지점에 도착할 수 있는 상태
dp = [1, 0, 0, 0, 0, 0, 0, 0]


def next(state):
    temp = [0 for i in range(8)]

    temp[0] = state[1] + state[2]
    temp[1] = state[0] + state[2] + state[3]
    temp[2] = state[0] + state[1] + state[3] + state[4]
    temp[3] = state[1] + state[2] + state[4] + state[5]
    temp[4] = state[2] + state[3] + state[5] + state[6]
    temp[5] = state[3] + state[4] + state[7]
    temp[6] = state[4] + state[7]
    temp[7] = state[5] + state[6]

    for i in range(8):
        temp[i] %= 100000007

    return temp


for i in range(int(input())):
    dp = next(dp)

print(dp[0])
