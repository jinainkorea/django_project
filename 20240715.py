# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

def solution(n):
    sum = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            sum += i

    return sum
print(solution(5))



# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
def solution1(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum
print(solution1(3, 5))



# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
def solution2(n):
    answer = ''
    for i in range(n):
        if (i % 2) == 0:
            answer += '수'
        else:
            answer += '박'
    return answer
print(solution2(5))

print("안녕하세요"[:4])


sum = 0
for i in range(6):
    if i % 2 == 0:
        continue
    sum += i
print(sum)


# 문제 : 사용자에게 숫자 3개를 입력받아서, 더한 결과를 출력해주세요. map, strip를 사용해주세요.
# a = map(int, input().strip().split(" "))
#
# print(list(a))


# 1. 본인의 나이를 입력받고 출력하는 기능을 구현하기
# input: 35
# 출력: 35 살 입니다.
# age = int(input().strip())
#
# print(f"{age} 살 입니다.")

# 2. 본인의 나이를 입력받고 출력하는 기능을 구현하기
# input: 35 180
# 출력: 35 살이며 180CM 입니다.
# age, height = map(int, input().strip().split(" "))
#
# print(f"{age} 살이며 {height}CM 입니다.")



'''
문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
조건 : 1월 ~ 3월까지
조건 : 2월의 마지막은 28일로 함
조건 : 첫 데이터의 key는 "1월", value는 31
'''
dic = {'1월':31, '2월':28, '3월':31}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
for key in dic:
    print(f"{key}은 {dic[key]}일까지 있다.")
for key, value in dic.items():
    print(f"{key}은 {value}일까지 있다.")



'''
문제 : 영수, 영희, 철수, 민수의 나이를 딕셔너리에 담기
조건 : 가장 효율적인 데이터 구조를 유지해주세요.
조건 : 변수명을 명확하고 간결하게 지어주세요.
조건 : 영수 11살
조건 : 영희 12살
조건 : 철수 13살
조건 : 민수 14살
'''
dic = {'영수':11, '영희':12, '철수':13, '민수':14}

'''
문제2 : 딕셔너리 순회 출력
'''
for key, value in dic.items():
    print(f"{key}는 {value}살")

'''
문제3 : 딕셔너리 아래 내용으로 수정
조건 : 영수 12살
조건 : 영희 12살
조건 : 영철 32살
조건 : 철수 13살
조건 : 민수 20살
'''
dic.update({'영수':12, '영철':32, '민수':20})
print(dic)



# 하샤드 수 판별하기
def solution5(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x % sum == 0:
        return True
    else:
        return False

print(solution5(13))