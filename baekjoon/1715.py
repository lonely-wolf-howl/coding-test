# https://www.acmicpc.net/problem/1715
# huffman coding

from queue import PriorityQueue

n = int(input())

min_heap = PriorityQueue()

for _ in range(n):
    deck_size = int(input())
    min_heap.put(deck_size)

total_cost = 0
# keep combining until only one deck is left
while min_heap.qsize() > 1:
    smallest = min_heap.get()
    next_smallest = min_heap.get()

    # merge them into one deck
    merged = smallest + next_smallest
    min_heap.put(merged)

    total_cost += merged

print(total_cost)
