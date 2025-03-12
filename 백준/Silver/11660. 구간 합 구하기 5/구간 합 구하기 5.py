import sys

# 1. 입력처리
N, M = map(int, sys.stdin.readline().strip().split())
numbers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
S = [[0] * N for _ in range(N)]

# 2. 구간합배열 구하기
for i in range(N):
    for j in range(N):
        if i ==0 and j == 0:
            S[i][j] = numbers[i][j]
        elif i == 0:
            S[i][j] = S[i][j-1] + numbers[i][j]
        elif j == 0:
            S[i][j] = S[i-1][j] + numbers[i][j]
        else:
            S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + numbers[i][j]
                        
# 3. 구간 입력받고 구간합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    result = S[x2-1][y2-1] 
    if x1 > 1 :
        result -= S[x1-2][y2-1]
    if y1 > 1 :
        result -= S[x2-1][y1-2]
    if x1 > 1 and y1 > 1:
        result += S[x1-2][y1-2] 
    print(result)
