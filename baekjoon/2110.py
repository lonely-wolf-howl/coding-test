# https://www.acmicpc.net/problem/2110

n, c = list(map(int, input().split(" ")))

"""
read house positions and sort them
"""
array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

"""
initialize binary search range
"""
start = 1  # minimum possible distance
end = array[-1] - array[0]  # maximum possible distance

result = 0  # the largest minimum distance found

"""
binary search to find the largest minimum distance
"""
while start <= end:
    mid: int = (start + end) // 2  # candidate distance
    value = array[0]  # position of the last placed router
    count = 1  # number of routers placed

    """
    try to place routers using the current candidate distance
    """
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]  # place router here
            count += 1  # increase router count

    """
    check if we can place at least c routers
    """
    if count >= c:  # can place at least c routers
        start = mid + 1  # try to find a larger distance
        result = mid
    else:  # cannot place enough routers
        end = mid - 1  # try to find a smaller distance

print(result)
