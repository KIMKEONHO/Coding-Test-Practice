import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀함수 사용할 때 제한 풀어주기 위해서
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    lst = [[0 for _ in range(M)] for _ in range(N)]  # N x M 크기
    visit = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        lst[y][x] = 1  # y는 세로, x는 가로

    def dfs(lst, visit, x, y):
        if x < 0 or y < 0 or x >= N or y >= M:  # x는 N, y는 M
            return 0
        if lst[x][y] == 0 or visit[x][y] == 1:
            return 0
        visit[x][y] = 1
        count = 1
        count += dfs(lst, visit, x + 1, y)
        count += dfs(lst, visit, x, y + 1)
        count += dfs(lst, visit, x, y - 1)
        count += dfs(lst, visit, x - 1, y)
        return count

    ans = []
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1 and visit[i][j] == 0:
                ans.append(dfs(lst, visit, i, j))

    print(len(ans))

