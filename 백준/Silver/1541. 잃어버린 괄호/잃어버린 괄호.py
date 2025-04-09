import sys

F = list(sys.stdin.readline().strip().split("-"))

# 첫 번째 항은 '+' 기준으로 쪼개서 합을 구함
result = sum(map(int, F[0].split("+")))

# 그 다음 항들부터는 '+' 기준으로 쪼갠 값을 모두 더해서 빼기
for f in F[1:]:
    result -= sum(map(int, f.split("+")))

print(result)
