import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))

lst.sort()

for lt in lst:
    print(lt[0], lt[1])
