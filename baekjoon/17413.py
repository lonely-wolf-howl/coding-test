# 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413

"""
예제 입력
baekjoon online judge
"""

S = input()

temp_str: str = ""
answer: str = ""
inside_tag: bool = False

for char in S:
    if char == "<":
        answer += temp_str[::-1] + "<"
        temp_str = ""
        inside_tag = True
    elif char == ">":
        answer += ">"
        inside_tag = False
    elif char == " ":
        if inside_tag:
            answer += " "
        else:
            answer += temp_str[::-1] + " "
            temp_str = ""
    else:
        if inside_tag:
            answer += char
        else:
            temp_str += char

answer += temp_str[::-1]

print(answer)
