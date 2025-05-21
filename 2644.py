import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

people = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    people[x].append(y)



def dfs(node, people, target):
    for i in people[node]:
        if i == target:
            return 2
        else:
            dfs(i, people, target)


print(people)