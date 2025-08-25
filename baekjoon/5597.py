# https://www.acmicpc.net/problem/5597

check = [0] * 31

for i in range(28):
    n = int(input())
    check[n] += 1

answer = []

for i in range(1, 31):
    if check[i] == 0:
        answer.append(i)

print(answer[0])
print(answer[1])
