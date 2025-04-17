import sys  
from collections import deque

# 1. 총 명령어 개수를 입력받아 정수로 변환
N = int(sys.stdin.readline().strip())

# 2. 큐을 구현할 deque 선언 , 인덱스
queue_deque = deque()  

# 3. 명령어 개수(N)만큼 반복하여 입력을 받고 실행
for _ in range(N):
    com = sys.stdin.readline().strip().split() 
    
    if com[0] == "size":
        print(len(queue_deque))
    
    elif com[0] == "empty":
        print(1 if not queue_deque else 0)
    
    elif com[0] == "front":
        print(queue_deque[0] if queue_deque else -1) 

    elif com[0] == "back":
        print(queue_deque[-1] if queue_deque else -1)  
    
    elif com[0] == "push":
        queue_deque.append(int(com[1]))  
        
    elif com[0] == "pop":
        print(queue_deque.popleft() if queue_deque else -1) 