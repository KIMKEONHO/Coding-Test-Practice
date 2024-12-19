import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m # m 으로 나눴을 때 남는 나머지의 갯수 만큼 생성
ans = 0

S[0] = A[0]
for i in range(1,n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        ans += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        ans += (C[i] * (C[i]-1) // 2) # //사용으로 소숫점 제거

print(ans)