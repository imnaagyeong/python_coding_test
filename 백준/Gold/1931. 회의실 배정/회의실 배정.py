import sys

n = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 종료 시간 기준, 같으면 시작 시간 기준 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)