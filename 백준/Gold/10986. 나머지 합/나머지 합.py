import sys

# 1. 입력값 처리
N, M = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))

# 2. 누적합을 M으로 나눈 나머지 개수를 저장할 배열
mod_count = [0] * M  # 나머지 값(0~M-1)의 개수를 저장
mod_count[0] = 1 # 누적합이 처음부터 M의 배수일 경우를 위해 미리 1 설정

S = 0 # 누적합
result = 0 # 결과

# 3. 누적합을 구하면서 나머지를 세기
for num in numbers:
    S += num
    result += mod_count[S % M]
    mod_count[S%M] += 1

print(result)