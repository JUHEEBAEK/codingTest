# 아침코테 #코드업 #파이썬 #기초100제 #종합 #짝수의합구하기

# 타이틀: 6077 [기초-종합] 짝수 합 구하기
# 문제: 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

'''
참고
while 이나 for 반복실행구조를 이용할 수 있다.
다른 방법이나 while 반복실행구조를 이용해서도 성공시켜 보자.

입력
정수 1개가 입력된다.
(0 ~ 100)

출력
1부터 그 수까지 짝수만 합해 출력한다.
'''

# 입력 예시
# 5

# 출력 예시
# 6

inputNum = int(input())

i = 1
sum = 0

while(i <= inputNum):
    if i % 2 == 0:
        sum += i

    i = i + 1

print(sum)

# or

for i in range(inputNum + 1):
    if i % 2 == 0:
        sum += i

print(sum)
