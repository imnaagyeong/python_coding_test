import sys

N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 예외 처리: 계단이 1개 또는 2개일 경우
if N == 1:
    print(nums[0])
    sys.exit()
elif N == 2:
    print(nums[0] + nums[1])
    sys.exit()

# DP 테이블 초기화
dp = [0] * N
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(nums[0] + nums[2], nums[1] + nums[2])  # 첫 번째 + 세 번째 or 두 번째 + 세 번째

# 점화식 적용
for i in range(3, N):
    dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i])

print(dp[N-1])
