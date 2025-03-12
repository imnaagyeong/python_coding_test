import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

print((sum(numbers) * 100)/(max(numbers)*N))