# https://www.acmicpc.net/problem/1874

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
operations = []
current = 1

is_possible = True

for target in sequence:
    while current <= target:
        stack.append(current)
        operations.append("+")
        current += 1

    if stack[-1] == target:
        stack.pop()
        operations.append("-")
    else:
        is_possible = False
        break

if is_possible:
    print("\n".join(operations))
else:
    print("NO")
