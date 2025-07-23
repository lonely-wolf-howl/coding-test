# https://www.acmicpc.net/problem/1302

N = int(input())

books: dict = {}

for i in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1


target = max(books.values())
result = []

for book, count in books.items():
    if count == target:
        result.append(book)

print(sorted(result)[0])
