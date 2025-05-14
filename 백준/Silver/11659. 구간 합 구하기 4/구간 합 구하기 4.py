import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 배열 만들기 (0번째는 0으로 시작)
prefix_sum = [0]
for num in nums:
    prefix_sum.append(prefix_sum[-1] + num)

for _ in range(M):
    A, B = map(int, input().split())
    print(prefix_sum[B] - prefix_sum[A - 1])