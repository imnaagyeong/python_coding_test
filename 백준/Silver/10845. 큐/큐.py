import sys  
from collections import deque

# 1. 총 명령어 개수를 입력받아 정수로 변환
N = int(sys.stdin.readline().strip())

# 2. 큐을 구현할 deque 선언 , 인덱스
arr = deque()  

# 3. 명령어 개수(N)만큼 반복하여 입력을 받고 실행
for _ in range(N):
    com = sys.stdin.readline().strip().split() 
    
    if com[0] == "size":
        print(len(arr))
    
    elif com[0] == "empty":
        print(1 if not arr else 0)
    
    elif com[0] == "front":
        print(arr[0] if arr else -1) 

    elif com[0] == "back":
        print(arr[-1] if arr else -1)  
    
    elif com[0] == "push":
        arr.append(int(com[1]))  
        
    elif com[0] == "pop":
        print(arr.popleft() if arr else -1) 