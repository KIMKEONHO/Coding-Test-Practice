import sys
from queue import PriorityQueue
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    s, e, v = map(int, input().split())
    pq.put((v, s, e)) # 가중치 기준 정렬을 위해 v를 제일 앞에 둔다

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # return find(parent[a])로 표현하지 않은 이유는 find연산시 경로 압축하기 위해서
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N - 1 and not pq.empty():
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s,e)
        result += v
        useEdge += 1

print(result)