import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

bigger = [[] for _ in range(N + 1)]
smaller = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    bigger[a].append(b)
    smaller[b].append(a)

def dfs(start, graph, visited):
    stack = [start]
    count = 0
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                count += 1
    return count

result = 0

for i in range(1, N + 1):
    visited_big = [False] * (N + 1)
    visited_sml = [False] * (N + 1)

    big_count = dfs(i, bigger, visited_big)
    sml_count = dfs(i, smaller, visited_sml)

    if big_count + sml_count == N - 1:
        result += 1

print(result)
