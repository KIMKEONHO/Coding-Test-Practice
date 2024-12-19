import sys
sys.setrecursionlimit(10**6) #재귀함수 사용할 때 제한 풀어주기 위해서
input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
tree = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

for _ in range(1, N): # 인접 리스트로 저장
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

#DFS
def DFS(number):
    visited[number] = True
    for i in tree[number]:
        if not visited[i]:
            answer[i] = number
            DFS(i)

DFS(1)

for i in range(2, N+1):
    print(answer[i])