import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

# 각 문자별로 누적 합 배열 생성
prefix_sum = [[0] * 26 for _ in range(len(S) + 1)]

# 누적 합 계산
for i in range(len(S)):
    for j in range(26):
        prefix_sum[i + 1][j] = prefix_sum[i][j]
    prefix_sum[i + 1][ord(S[i]) - ord('a')] += 1

# 쿼리 처리
for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    alpha_idx = ord(alpha) - ord('a')
    
    # r+1 위치까지의 합에서 l 위치까지의 합을 빼서 구간 합 계산
    result = prefix_sum[r + 1][alpha_idx] - prefix_sum[l][alpha_idx]
    print(result)
