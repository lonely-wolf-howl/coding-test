# 바이러스
# https://www.acmicpc.net/problem/2606


def adjacency_list(num, edges):
    graph = {i: [] for i in range(1, num + 1)}

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return visited


if __name__ == "__main__":
    num = int(input())
    network = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(network)]
    """
    [(1, 2), (2, 3), (1, 5), (5, 2), (5, 6), (4, 7)]
    """

    graph = adjacency_list(num, edges)
    """
    {
        1: [2, 5],
        2: [1, 3, 5],
        3: [2],
        4: [7],
        5: [1, 2, 6],
        6: [5],
        7: [4]
    }
    """

    infected: set = dfs(graph, 1)
    """
    {1, 2, 3, 5, 6}
    """

    print(len(infected) - 1)
