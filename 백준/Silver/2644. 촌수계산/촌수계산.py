import sys

# 1. 입력처리
n = int(sys.stdin.readline().strip()) # 전체 사람의 수
a, b = map(int, sys.stdin.readline().strip().split()) # 촌수를 계산할 두사람
m = int(sys.stdin.readline().strip()) # 부모-자식 관계의 수

graph = {i: [] for i in range(1, n + 1)}  

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split()) # 부모 i, 자식 j
    graph[i].append(j)
    graph[j].append(i)

# 2. a와 b의 촌 수 계산하기
stack = [(a, 0)]  # (현재 노드, 촌수)
visited = set()

while stack:
    v, count = stack.pop()
        
    if v == b:  # b를 찾으면 촌수 출력
        print(count)
        break
        
    if v not in visited:
        visited.add(v)
        # 인접한 노드들을 스택에 넣음
        for neighbor in graph[v]:
            if neighbor not in visited:
                stack.append((neighbor, count + 1))
else:
    print(-1)