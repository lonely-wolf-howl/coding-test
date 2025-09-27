# https://www.acmicpc.net/problem/1417

from queue import PriorityQueue

"""
3
5
7
7
"""

n = int(input())

votes = [0] * n

for i in range(n):
    votes[i] = int(input())

# votes
# [5, 7, 7]

pq = PriorityQueue()

for i in range(1, n):
    pq.put(-votes[i])  # max-heap

# pq.qsize()
# 2
# pq.get()
# -7

if n == 1:
    print(0)
else:
    bribe_count = 0  # number of votes to buy
    while True:
        max_votes = -pq.get()  # get the current highest votes
        if max_votes < votes[0]:
            break  # stop if first candidate already leads

        max_votes -= 1
        votes[0] += 1
        bribe_count += 1
        pq.put(-max_votes)

    print(bribe_count)
