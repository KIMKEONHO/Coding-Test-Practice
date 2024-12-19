import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
V = int(input())

graph = [[] for _ in range(N + 1)]
ans = []
for i in range(V):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(graph,ans):
    visited = [False] * (N + 1)
    stack = [1]
    visited[1] = True
    while stack:
        node = stack.pop()
        ans.append(node)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    return(ans)

print(len(dfs(graph,ans)) - 1)