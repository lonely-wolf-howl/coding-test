# https://www.acmicpc.net/problem/7490

"""
예시 입력
2
3
7
"""

import copy


def recursive(arr, n):
    if len(arr) == n:
        operators_list.append(copy.deepcopy(arr))
        return

    arr.append(" ")
    recursive(arr, n)
    arr.pop()

    arr.append("+")
    recursive(arr, n)
    arr.pop()

    arr.append("-")
    recursive(arr, n)
    arr.pop()


test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1)

    intergers = [i for i in range(1, n + 1)]

    for operators in operators_list:
        """
        # operators_list
            [
                [' ', ' '], [' ', '+'], [' ', '-'],
                ['+', ' '], ['+', '+'], ['+', '-'],
                ['-', ' '], ['-', '+'], ['-', '-']
            ]
        # operators
            ['+', '-']
        """
        string = ""

        for i in range(n - 1):
            string += str(intergers[i]) + operators[i]
            """
            i = 0:
                string = "" + "1" + "+" → "1+"
            i = 1:
                string = "1+" + "2" + "-" → "1+2-"
            """
        string += str(intergers[-1])
        """
        string = "1+2-" + "3" → "1+2-3"
        """

        if eval(string.replace(" ", "")) == 0:
            print(string)

    print()
