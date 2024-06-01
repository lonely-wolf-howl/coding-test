# 키로거

"""
예제 입력
2
<<BP<A>>Cd-
ThIsIsS3Cr3t
"""

test_case = int(input())

for _ in range(test_case):
    password_input = str(input())

    left_stack = []
    right_stack = []

    for i in password_input:
        if i == "-":
            if left_stack:
                left_stack.pop()
        elif i == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))

    print("".join(left_stack))
