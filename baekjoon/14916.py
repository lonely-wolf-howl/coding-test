# https://www.acmicpc.net/problem/14916

n = int(input().strip())

if n in (1, 3):
    print(-1)
else:
    # q = number of 'five' coins, r = remainder
    q, r = divmod(n, 5)

    if r % 2 == 0:
        print(q + (r // 2))
    else:
        if q == 0:
            print(-1)
        else:
            q = q - 1
            r += 5
            print(q + (r // 2))
