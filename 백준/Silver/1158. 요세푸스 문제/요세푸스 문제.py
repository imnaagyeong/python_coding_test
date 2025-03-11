import sys  
from collections import deque

# 1. 사람 수, 제거할 번호 입력받아 정수로 변환
N, K = map(int, sys.stdin.readline().strip().split())

# 2 people deque 선언 & result list 선언
poeple = deque(range(1, N + 1))
result = list()
 
# 3. 사람 수(N)만큼 반복하여 원에서 사람을 제거
for _ in range(N):
    # k번째 전까진 pop해서 스택 뒤에 추가함
    for _ in range(K - 1):
        poeple.append(poeple.popleft())
    
    # K번째 요소 제거 & 결과 리스트에 추가
    result.append(poeple.popleft())
            

# 4. 최종 문자열 생성 & 출력
print("<" + ", ".join(map(str, result)) + ">")