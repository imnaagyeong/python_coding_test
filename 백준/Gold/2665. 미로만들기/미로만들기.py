import sys
from collections import deque

# 1. 입력 처리
n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]  # 공백 없이 들어온 경우

# 2. 변수 선언
check_room = deque([(0, 0)])  # (x, y) 위치
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하좌우 탐색
change_room = [[float('inf')] * n for _ in range(n)]
change_room[0][0] = 0  # 시작점 (0,0)은 변환할 필요 없음

# 3. 0-1 BFS 실행
while check_room:
    x, y = check_room.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            new_change = change_room[x][y] + (grid[nx][ny] == 0)  # 검은 방(0)이면 비용 증가

            if new_change < change_room[nx][ny]:  
                change_room[nx][ny] = new_change
                if grid[nx][ny] == 1:  # 흰 방이면 큐 뒤에 추가
                    check_room.append((nx, ny))
                else:  # 검은 방이면 큐 앞에 추가
                    check_room.appendleft((nx, ny))

# 4. 정답 출력
print(change_room[n-1][n-1])
