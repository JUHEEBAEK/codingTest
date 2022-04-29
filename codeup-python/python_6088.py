# 아침코테 #코드업 #파이썬 #기초100제 #종합 #수나열하기1

# 타이틀: 6085 : [기초-종합] 수 나열하기1
# 문제: 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.

# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

'''
1 4 7 10 13 16 19 22 25 ... 은
1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다.
이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여

등차(차이가 같다의 한문 말) 수열이라고 한다. (등차수열 : arithmetic progression/sequence)
수열을 알게 된 영일이는 갑자기 궁금해졌다.

"그럼.... 123번째 나오는 수는 뭘까?"

영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.

입력
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 100)

출력
n번째 수를 출력한다.

'''

# 입력 예시
# 1 3 5

# 출력 예시
# 13

startNum, differ, lastIndex = input().split()

startNum = int(startNum)
differ = int(differ)
lastIndex = int(lastIndex)

n = startNum - (differ * 1)

for i in range(lastIndex+1):
    if i == lastIndex:
        print(differ * i + n)
