import sys
from collections import *

N = int(sys.stdin.readline())


a = map(int, sys.stdin.readline().split())
T,P = map(int, sys.stdin.readline().split())
sum = 0
for i in a:
    if i < T:
        sum = sum + 1
    else:
        sum = sum + round(i+T - 1) // T

print(sum)
print(int(N//P), N%P)


