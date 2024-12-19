import sys
input = sys.stdin.readline

N = int(input())
lst = []
visit = [[0] * N for _ in range(N)]

for i in range(N):
    a = list(map(int, input().strip()))
    lst.append(a)

def dfs(lst, visit, i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return 0
    if visit[i][j] == 1 or lst[i][j] == 0:
        return 0
    visit[i][j] = 1
    count = 1

    count += dfs(lst, visit, i + 1, j)
    count += dfs(lst, visit, i - 1, j)
    count += dfs(lst, visit, i, j + 1)
    count += dfs(lst, visit, i, j - 1)

    return count

ans = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1 and visit[i][j] == 0:
            ans.append(dfs(lst, visit, i, j))

ans.sort()
print(len(ans))
for count in ans:
    print(count)
