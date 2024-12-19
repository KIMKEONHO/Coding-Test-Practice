import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
numbers2 = list(map(int, sys.stdin.readline().split()))

number_counts = Counter(numbers)

result = [number_counts.get(j, 0) for j in numbers2]

print(' '.join(map(str, result)))
