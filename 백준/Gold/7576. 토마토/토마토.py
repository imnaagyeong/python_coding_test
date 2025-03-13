import sys
from collections import deque

# 1. 입력값 처리 & 변수선언
N, M = map(int, sys.stdin.readline().strip().split())

# 2. 초기 토마토 상태 패딩 추가 & 익은/없는 토마토 위치 파악
tomatoes = [[-1] * (N + 2) for _ in range(M + 2)]  # 패딩처리된 토마토 상태
a_red_tomatoes = set()  # 확인 완료된 익은 토마토 위치
b_red_tomatoes = deque()  # 확인 전 익은 토마토 위치
no_tomatoes_count = 0

for i in range(1, M + 1):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        tomatoes[i][j + 1] = row[j] 
        if row[j] == 1:
            b_red_tomatoes.append((i, j + 1)) 
        elif row[j] == -1:
            no_tomatoes_count += 1 

# 3. 토마토가 익는데 걸리는 날짜 구하기
days = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
total_tomatoes = (N * M) - no_tomatoes_count  # 총 토마토 수
ripe_tomatoes = len(b_red_tomatoes)  # 현재 익은 토마토 수

while ripe_tomatoes < total_tomatoes:
    new_red_tomatoes = deque()  # 새롭게 익은 토마토 저장

    while b_red_tomatoes:
        i, j = b_red_tomatoes.popleft()  # 현재 익은 토마토

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if tomatoes[ni][nj] == 0:  # 익지 않은 토마토인 경우
                tomatoes[ni][nj] = 1  # 익음 처리
                new_red_tomatoes.append((ni, nj))  # 새 익은 토마토 추가

    if not new_red_tomatoes:  # 더 이상 익힐 토마토가 없으면
        print(-1)
        exit()

    b_red_tomatoes = new_red_tomatoes  # 새로운 익은 토마토 저장
    ripe_tomatoes += len(b_red_tomatoes)  # 익은 토마토 수 업데이트
    days += 1  # 하루 증가

print(days)