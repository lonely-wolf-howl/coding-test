# https://www.acmicpc.net/problem/1343

board = str(input())

answer = ""
count = 0
possible = True

for i in board:
    if i == "X":
        count += 1
        if count == 4:
            answer += "AAAA"
            count = 0
    else:  # i == "."
        if count == 1 or count == 3:
            possible = False
            break
        elif count == 2:
            answer += "BB"
        count = 0
        answer += "."

if possible:
    if count == 1 or count == 3:
        possible = False
    elif count == 2:
        answer += "BB"

print(answer if possible else -1)
