# 하샤드 수 판별하기 - 10진법 이용
def solution(x):
    sum = 0
    share = x
    remain = 0
    while share != 0:
        remain = share % 10
        share //= 10
        sum += int(remain)
    if x % sum == 0:
        return True
    else:
        return False

print(solution(13))

