import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip()))
result = 0

for i in range(N):
   result += numbers[i]

print(result) 