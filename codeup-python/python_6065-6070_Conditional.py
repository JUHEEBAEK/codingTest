# 아침코테 #코드업 #파이썬 #기초100제 #조건문 #선택실행조건


# 타이틀: 6065 [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
# 문제: 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

# if문
'''
if 조건식 :
  실행1  #조건식의 평가값이 True 인 경우 실행시킬 명령을 들여쓰기를 이용해 순서대로 작성한다.
  실행2
실행3  #들여쓰기를 하지 않은 부분은 조건식에 상관이 없음

python 에서는 논리적 실행단위인 코드블록(code block)을 표현하기 위해 들여쓰기를 사용한다.
들여쓰기 방법은 탭(tab), 공백(space) 4개 등 여러 가지 방법을 사용할 수 있지만
한 소스코드 내에서 들여쓰기 길이와 방법은 똑같아야 한다. 

참고 
a%2==0 은 (a%2)가 먼저 계산된 후 그 결과를 정수 0과 비교한 결과값이다.
a를 2로 나눈 나머지가 0, 즉 짝수이면 True 가 되고, 아니면 False 로 계산된다.
따라서,
if a%2==0 : #a가 짝수라면 ... 
와 같은 의미가 된다. 짝수가 아니라면 들여쓰기로 작성된 부분들은 실행되지 않는다.

입력
3개의 정수(a, b, c)가 공백을 두고 입력된다.
0 ~ +2147483647 범위의 정수들이 입력되며 적어도 1개는 짝수이다.

출력
짝수만 순서대로 줄을 바꿔 출력한다.

'''

# 입력 예시
# 1 2 4

# 출력 예시
# 2
# 4

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if(a % 2 == 0):
    print(a)
if(b % 2 == 0):
    print(b)
if(c % 2 == 0):
    print(c)


# 타이틀: 6066 [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
# 문제: 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.


# if else문
'''
if 조건식 :  #조건식을 평가해서...
  실행1      #True 인 경우 실행시킬 명령들...
  실행2
else :        
  실행3      #False 인 경우 실행시킬 명령들...
  실행4
실행5       #조건식과 상관없는 다음 명령 

else 는 if 없이 혼자 사용되지 않는다.
또한, else 다음에는 조건식이 없는 이유는? True(참)가 아니면 False(거짓)이기 때문에... 
조건식의 평가 결과는 True 아니면 False 로 계산되기 때문이다.

python 에서는 들여쓰기를 기준으로 코드블록을 구분하므로, 들여쓰기를 정확하게 해주어야 한다.

입력
3개의 정수(a, b, c)가 공백을 두고 입력된다.
0 <= a,b,c <= 2147483647

출력
입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.
'''

# 입력 예시
# 1 2 8

# 출력 예시
# odd
# even
# even

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if(a % 2 == 0):
    print("even")
else:
    print("odd")

if(b % 2 == 0):
    print("even")
else:
    print("odd")

if(c % 2 == 0):
    print("even")
else:
    print("odd")

# 타이틀: 6067 [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
# 문제: 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자. 음수이면서 짝수이면, A
#      음수이면서 홀수이면, B 양수이면서 짝수이면, C 양수이면서 홀수이면, D를 출력한다.


'''
참고
조건/선택 실행구조 안에 다시 조건/선택 실행구조를 "중첩"할 수가 있다.

또한, 중첩된 조건은
...
if (n<0) and (n%2==0) :
    print('A')
...
와 같이 논리연산자(not, and, or)를 이용해 합쳐 표현할 수도 있다.
비교연산(<, >, <=, >=, ==, !=) 의 계산 결과는 True 또는 False 의 불(boolean) 값이고,
불 값들 사이의 논리연산(not, and, or)의 결과도 True 또는 False 의 불 값이다.

입력
정수 1개가 입력된다.
-2147483648 ~ +2147483647, 단 0은 입력되지 않는다.

출력
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.
'''

# 입력 예시
# -2147483648

# 출력 예시
# A

a = input()
a = int(a)

if(a < 0) and (a % 2 == 0):
    print("A")
if(a < 0) and (a % 2 == 1):
    print("B")
if(a > 0) and (a % 2 == 0):
    print("C")
if(a > 0) and (a % 2 == 1):
    print("D")


# 타이틀: 6068 [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기
# 문제: 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
#      평가 기준
#      점수 범위 : 평가
#      90 ~ 100 : A
#      70 ~   89 : B
#      40 ~   69 : C
#      0 ~   39 : D
#      로 평가되어야 한다.

'''
참고
if 조건식1 : 
  ... 
elif 조건식2 : 
  ... 
elif 조건식3 : 
  ... 
else : 
  ...
도 똑같은 기능을 한다. elif는 else if 의 짧은 약어라고 생각해도 된다.
elif 를 사용하면 if ... else ... 구조를 겹쳐 사용할 때처럼, 여러 번 안 쪽으로 들여쓰기 하지 않아도 된다.

입력
정수(0 ~ 100) 1개가 입력된다.

출력
평가 결과를 출력한다.
'''

# 입력 예시
# 73

# 출력 예시
# B

a = input()
a = int(a)

if a >= 90:
    print("A")
elif a >= 70:
    print("B")
elif a >= 40:
    print("C")
else:
    print("D")


# 타이틀: 6069 [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
# 문제: 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

'''
평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

입력
영문자 1개가 입력된다.
(A, B, C, D 등 문자 1개가 입력된다.)

출력
문자에 따라 다른 내용이 출력된다.

'''

# 입력 예시
# A

# 출력 예시
# best!!!

c = input()

if c == "A":
    print("best!!!")
elif c == "B":
    print("good!!")
elif c == "C":
    print("run!")
elif c == "D":
    print("slowly~")
else:
    print("what?")


# 타이틀: 6070 [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
# 문제: 월이 입력될 때 계절 이름이 출력되도록 해보자.
#       월 : 계절 이름
#       12, 1, 2 : winter
#        3, 4, 5 : spring
#        6, 7, 8 : summer
#        9, 10, 11 : fall


'''
참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

입력
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

출력
계절 이름을 출력한다.
'''

# 입력 예시
# 12

# 출력 예시
# winter

a = input()
a = int(a)

if(a == 12 or a == 1 or a == 2):
    print("winter")
elif (a == 3 or a == 4 or a == 5):  # elif(a//3 == 1) 이렇게 풀수도 있음.
    print("spring")
elif (a//3 == 2):
    print("summer")
elif (a//3 == 3):
    print("fall")
