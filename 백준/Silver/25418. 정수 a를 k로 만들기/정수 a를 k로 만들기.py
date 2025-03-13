import sys
from collections import deque

# 1. 입력 처리
A, K = map(int, sys.stdin.readline().strip().split())

# 2. 변수 선언
numbers = deque([A])
visited = set([A])  # 중복 체크용 set()
count = 0

# 3. BFS 탐색
while numbers:
    count += 1
    for _ in range(len(numbers)): 
        num = numbers.popleft()
        if num + 1 == K or num * 2 == K:
            print(count)
            exit()
        
        # **K보다 큰 값은 탐색할 필요 없음!**
        if num + 1 <= K and num + 1 not in visited:
            numbers.append(num + 1)
            visited.add(num + 1)

        if num * 2 <= K and num * 2 not in visited:
            numbers.append(num * 2)
            visited.add(num * 2)
