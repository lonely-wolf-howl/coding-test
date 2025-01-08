# 스택 수열
# https://www.acmicpc.net/problem/1874

"""
예제 입력
8
4
3
6
8
7
5
2
1
"""

n = int(input())  # 8
sequence = list(int(input()) for _ in range(n))  # [4, 3, 6, 8, 7, 5, 2, 1]

stack = []
result = []
current = 1
possible = True

for number in sequence:
    while current <= number:
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == number:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")

"""
+ push 1 (current=1): stack = [1         ], result = ['+'                    ], current = 2
+ push 2 (current=2): stack = [1, 2      ], result = ['+', '+'               ], current = 3
+ push 3 (current=3): stack = [1, 2, 3   ], result = ['+', '+', '+'          ], current = 4
+ push 4 (current=4): stack = [1, 2, 3, 4], result = ['+', '+', '+', '+'     ], current = 5
- pop  4            : stack = [1, 2, 3   ], result = ['+', '+', '+', '+', '-'], current = 5
"""
