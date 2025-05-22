import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, K = map(int, input().split())

lst = [[0] * M for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    lst[a-1][b-1] = 1

result = []

def dfs(y, x):
    lst[y][x] = 0
    count = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == 1:
            count += dfs(ny, nx)
    return count

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            result.append(dfs(i, j))

print(max(result) if result else 0)