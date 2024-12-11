# 걸그룹 마스터 준석이
# https://www.acmicpc.net/problem/16165

N, M = map(int, input().split())

team_member, member_team = {}, {}

for i in range(N):
    team_name = input()
    member_number = int(input())

    team_member[team_name] = []

    for j in range(member_number):
        member_name = input()
        team_member[team_name].append(member_name)
        member_team[member_name] = team_name

for i in range(M):
    name = input()
    quiz = int(input())

    if quiz == 1:
        print(member_team[name])
    else:
        for member in sorted(team_member[name]):
            print(member)

# team_member
# {
#     "blackpink": ["jenny", "jisu", "lisa", "rose"],
# }

# member_team
# {
#     "jenny": "blackpink",
#     "jisu": "blackpink",
#     "lisa": "blackpink",
#     "rose": "blackpink",
# }
