import sys  
from collections import deque

# 1. 초기 문자열 입력받아서 왼쪽 deque로 선언, 오른쪽 deque도 선언
left = deque(sys.stdin.readline().strip())
right = deque() 

# 2. 총 명령어 개수를 입력받아 정수로 변환
M = int(sys.stdin.readline().strip())  

# 3. 명령어 개수(M)만큼 반복하여 입력을 받고 실행
for _ in range(M):
    com = sys.stdin.readline().strip().split()  

    if com[0] == "L":  # 왼쪽 이동
        if left:  
            right.appendleft(left.pop())
    
    elif com[0] == "D":  # 오른쪽 이동
        if right:
            left.append(right.popleft())
            
    elif com[0] == "B":  # 왼쪽 문자 삭제
        if left:
            left.pop()
            
    elif com[0] == "P":  # 문자 추가
        left.append(com[1])

# 4. 최종 문자열 생성 & 출력
print("".join(left) + "".join(right))
