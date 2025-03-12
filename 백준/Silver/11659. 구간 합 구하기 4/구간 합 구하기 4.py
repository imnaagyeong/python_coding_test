import sys

N, M = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
S = [0] * (N + 1)
for i in range(1, N+1):
    S[i] = S[i-1] + numbers[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(S[j] - S[i-1])