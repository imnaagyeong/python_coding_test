import sys
from collections import deque

# 1. 총 명령어 개수를 int로 저장한다.
N = int(sys.stdin.readline().strip())  
arr = deque()  # 리스트 대신 deque 사용

# 2. 명령어의 개수만큼 반복하면서 명령어를 받고 실행한다.
for _ in range(N):
    com = sys.stdin.readline().strip().split()  # 공백을 기준으로 명령어 분리
    
    if com[0] == "size":
        print(len(arr))
    
    elif com[0] == "empty":
        print(1 if not arr else 0)
    
    elif com[0] == "top":
        print(arr[-1] if arr else -1)  # 스택의 top 출력
    
    elif com[0] == "push":
        arr.append(int(com[1]))  # deque의 append() 사용
    
    elif com[0] == "pop":
        print(arr.pop() if arr else -1)  # pop() 수행
