import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]: # 새로들어온 수가 오큰수가 됨
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""
for i in range(N):
    result += str(ans[i]) + " "

print(result)