import sys

N = int(sys.stdin.readline())

lst = [[] for _ in range(201)]
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)

    lst[age].append(name)

for i in range(1, 201):
    if lst[i]:
        for name in lst[i]:
            print(f"{i} {name}")