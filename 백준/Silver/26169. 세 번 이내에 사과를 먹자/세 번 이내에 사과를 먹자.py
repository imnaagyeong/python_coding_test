import sys

# 1. 입력 처리
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
r, c = map(int, sys.stdin.readline().strip().split())
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 2. 세 번 이내에 사과를 먹을 수 있는지 구하기
stack = [(r, c, 0, 0)]  # 스택에는 (x, y, 이동 횟수, 사과 먹은 개수) 저장
visited = set()

while stack:
    i, j, move, apple = stack.pop()
    
    # 사과 2개를 먹었으면 결과 출력
    if apple >= 2:
        print(1)
        break

    # 이동 횟수가 3번을 넘으면 더 이상 진행할 필요 없음
    if move >= 3:
        continue
    
    if (i, j) not in visited:
        visited.add((i, j))  # 방문 처리
        board[i][j] = -1  # 이동 후 현재 위치를 -1로 바꿈

        # 상하좌우로 이동
        for x, y in directions:
            ni, nj = i + x, j + y

            # 범위 체크와 장애물 체크
            if 0 <= ni < 5 and 0 <= nj < 5:  # 범위 안에 있는지 확인
                if board[ni][nj] != -1:  # 장애물이 아닌 경우
                    # 사과를 먹은 경우
                    if board[ni][nj] == 1:
                        stack.append((ni, nj, move + 1, apple + 1))
                    else:  # 사과를 먹지 않은 경우
                        stack.append((ni, nj, move + 1, apple))
                    
else:
    # 사과를 2개 이상 먹을 수 없다면 끝내고 0 출력
    print(0)
