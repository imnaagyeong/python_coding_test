import sys
from collections import deque

K = int(sys.stdin.readline().strip())
nums = deque()
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))