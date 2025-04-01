import sys

# 1. 입력처리
N = int(sys.stdin.readline().strip()) 
nums = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]  

# 2. 예외처리
if N == 1: 
    print(nums[0][0])
    sys.exit()
    
# 3. 삼각형 최대합 구하기
dp = [[0]* N for _ in range(N)]
dp[0][0] = nums[0][0] 

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:  # 왼쪽 끝
            dp[i][j] = nums[i][j] + dp[i-1][j]
        elif j == i:  # 오른쪽 끝
            dp[i][j] = nums[i][j] + dp[i-1][j-1]
        else:  # 중간
            dp[i][j] = nums[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1])) 