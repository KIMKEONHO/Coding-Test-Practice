import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

w, h = map(int, input().split())


def dfs(grid, x, y, visit):
    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

    if grid[y][x] == 1 and not visit[y][x]:
        visit[y][x] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == 1 and not visit[ny][nx]:
                dfs(grid, nx, ny, visit)


while w != 0 and h != 0:
    grid = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False for _ in range(w)] for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visit[i][j]:
                dfs(grid, j, i, visit)
                count += 1

    print(count)
    w, h = map(int, input().split())
