import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())
page = [list(map(int,input().split())) for _ in range(n)]

def dfs(x, y):
    stack = [(x, y)]
    page[x][y] = 0
    count = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and page[nx][ny] == 1:
                page[nx][ny] = 0
                stack.append((nx, ny))
                count += 1
    return count

result = []
for i in range(n):
    for j in range(m):
        if page[i][j] == 1:
            result.append(dfs(i, j))

print(len(result))
print(max(result) if result else 0)
