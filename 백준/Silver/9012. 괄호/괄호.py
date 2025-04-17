import sys
from collections import deque

K = int(sys.stdin.readline().strip())

for _ in range(K):
    str_bracket = deque(sys.stdin.readline().strip())

    # 1. 개수 안 맞으면 바로 NO
    if str_bracket.count("(") != str_bracket.count(")"):
        print("NO")
        continue
    # 2. 끝이 )가 아니면 바로 NO
    if str_bracket[-1] != ")":
        print("NO")
        continue

    count = 0
    is_valid = True

    while str_bracket:
        ch = str_bracket.popleft()  # 앞에서부터 처리
        if ch == "(":
            count += 1
        else:
            count -= 1
        if count < 0:  # ')'가 '('보다 먼저 나온 경우
            is_valid = False
            break

    print("YES" if is_valid and count == 0 else "NO")