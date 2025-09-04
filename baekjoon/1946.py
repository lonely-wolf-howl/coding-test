# https://www.acmicpc.net/problem/1946

import sys
import math

read = sys.stdin.readline

t = int(read())

for _ in range(t):
    n = int(read())
    applicants = []
    for _ in range(n):
        document_rank, interview_rank = map(int, read().split())
        applicants.append((document_rank, interview_rank))

    applicants.sort(key=lambda x: x[0])
    # [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]

    best_interview_rank = math.inf
    selected_count = 0

    for _, interview_rank in applicants:
        if interview_rank < best_interview_rank:
            selected_count += 1
            best_interview_rank = interview_rank

    print(selected_count)
