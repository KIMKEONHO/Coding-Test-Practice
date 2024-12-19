import  sys

N,K = map(int,sys.stdin.readline().split())

sum = 1
sum2 = 1
for i in range(K):
    sum = sum * N
    N = N - 1
    sum2 = sum2 * K
    K = K - 1

print(int(sum/sum2))