import sys
from collections import deque

input = sys.stdin.readline

# 입력
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 간선 입력 및 무방향 그래프 구성
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 각 정점의 인접 리스트를 오름차순으로 정렬
for i in range(1, N + 1):
    graph[i].sort()


# DFS 함수 (반복문 + 스택 사용)
def dfs(start):
    visited = [False] * (N + 1)
    stack = [start]
    result = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            result.append(v)
            # 작은 노드부터 방문하기 위해 역순으로 스택에 추가
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return result


# BFS 함수 (큐 사용)
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)

        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


# DFS 결과 출력
dfs_result = dfs(V)
print(" ".join(map(str, dfs_result)))

# BFS 결과 출력
bfs_result = bfs(V)
print(" ".join(map(str, bfs_result)))
