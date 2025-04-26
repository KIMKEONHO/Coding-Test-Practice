import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

M, N, K = map(int, input().split())

page = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            page[y][x] = 1

def dfs(x, y, page):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    count = 1
    page[y][x] = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and page[ny][nx] == 0:
            count += dfs(nx, ny, page)

    return count

result = []

for i in range(M):
    for j in range(N):
        if page[i][j] == 0:
            result.append(dfs(j, i, page))

result.sort()
print(len(result))
print(" ".join(map(str, result)))
