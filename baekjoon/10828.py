# 스택

"""
예제 입력
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
"""

import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = input().strip().split(" ")  # 'push 1' => ['push', '1']

    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
