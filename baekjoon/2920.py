# 음계

import sys

input = sys.stdin.readline

D = list(map(int, input().split(" ")))

ascending = True
descending = True

# i = 1, 2, 3, 4, 5, 6, 7
for i in range(1, 8):
    if D[i - 1] < D[i]:
        descending = False
    elif D[i - 1] > D[i]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
