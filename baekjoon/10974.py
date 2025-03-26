# 모든 순열
# https://www.acmicpc.net/problem/10974


def dfs(N, permutation, visited):
    if len(permutation) == N:
        print(" ".join(map(str, permutation)))
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            permutation.append(i)

            dfs(N, permutation, visited)

            permutation.pop()
            visited[i] = False


if __name__ == "__main__":
    N = int(input())
    permutation = []
    visited = [False] * (N + 1)
    dfs(N, permutation, visited)
