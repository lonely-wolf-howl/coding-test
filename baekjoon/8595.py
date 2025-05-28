# 히든 넘버
# https://www.acmicpc.net/problem/8595

import sys

input = sys.stdin.readline

n = int(input())
word = input().strip()

total: int = 0
number: str = ""

for x in word:
    if x.isdigit():
        number += x
    else:
        if number:  # if the number string is not empty
            total += int(number)  # convert the number string to int and add to total
            number = ""  # reset the number string

if number:  # check again in case the string ends with digits
    total += int(number)

print(total)
