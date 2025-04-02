import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

# 1. 입력처리
N, M = map(int, input().strip().split())
heights = [list(map(int, input().strip().split())) for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
dp = [[-1] * M for _ in range(N)] # 값이 -1이면 방문하지 않음

def dfs(x, y):
    # 목적지에 도착하면 경로 1개 추가
    if x == N - 1 and y == M - 1:
        return 1
    
    # 이미 방문한 경우
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0 
    
    # 네 방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # 범위 안에 있고, 현재 위치보다 낮은 곳만 이동
        if 0 <= nx < N and 0 <= ny < M and heights[nx][ny] < heights[x][y]:
            dp[x][y] += dfs(nx, ny)  # 재귀적으로 경로 수 계산
    
    return dp[x][y]

print(dfs(0, 0))