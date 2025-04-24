import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
building = [list(map(int, input().split())) for _ in range(N)]
max_height = max(max(row) for row in building)

def dfs(x, y, water_level, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and building[nx][ny] > water_level:
            visited[nx][ny] = True
            dfs(nx, ny, water_level, visited)

max_area_count = 0

for water_level in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    area_count = 0

    for i in range(N):
        for j in range(N):
            if building[i][j] > water_level and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, water_level, visited)
                area_count += 1

    max_area_count = max(max_area_count, area_count)

print(max_area_count)
