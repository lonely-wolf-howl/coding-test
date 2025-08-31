# https://www.acmicpc.net/problem/18258

from collections import deque
import sys

queue = deque()
deq = deque()

n = int(input())

for i in range(n):
    command = sys.stdin.readline()
    command = command.split()

    if command[0] == "push":
        deq.append(command[1])
    if command[0] == "pop":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())
    if command[0] == "size":
        print(len(deq))
    if command[0] == "empty":
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    if command[0] == "front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    if command[0] == "back":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])
