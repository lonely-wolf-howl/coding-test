# https://www.acmicpc.net/problem/1427

"""
this code uses a simple form of counting sort.

# step 1: we loop through digits from 9 down to 0.
# step 2: for each digit (i), we check how many times it appears in N.
# step 3: if found, we print it as many times as it appears.
"""

N = input()

for i in range(9, -1, -1):
    for j in N:
        if int(j) == i:
            print(i, end="")
