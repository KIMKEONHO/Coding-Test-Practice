import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

def dfs(current, target, visited, total):
    if current == target:
        return total
    visited[current] = True
    for neighbor, cost in graph[current]:
        if not visited[neighbor]:
            result = dfs(neighbor, target, visited, total + cost)
            if result != -1:
                return result
    return -1

for _ in range(M):
    start, end = map(int, input().split())
    visited = [False] * (N + 1)
    print(dfs(start, end, visited, 0))