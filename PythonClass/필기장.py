# len함수: 리스트 변수 안에 요소들이 몇개인지 출력하는 함수
# 4장. 데이터 다루기
#  1. 파이썬에서 변수 사용법
#  2. 산술 연산자
#  3. 함수
#  4. Input 명령어 사용법
#    4.1 파이썬에서 변수 사용법
#       • 일반 변수: 변수안에 데이터가 한개
#         a = 1000
#         Print(a)
#         Print(type(a)) <class 'int'> 숫자 데이터 타입 < class 'str' > 문자 데이터 타입
#
#       • 리스트 변수: 변수 안에 여러개의 데이터가 들어있는 변수
#         D = [1000, 2000, 3000, 4000]
#               0     1     2     3  # 파이썬은 시작번호가 0임
#
#         Print(type(d)) <class 'list'> 리스트 데이터 타입
#
#       • 주의사항: 파이썬은 pl/sql이나 java처럼 세미콜론을 사용하지 않고 콜론사용.
#                 But 콜론: 반드시 써줘야 하는 경우 - If, while loop, for loop, def class(사용자정의함수)문 생성시 사용
#                 파이썬이 코드 간결한 이유는 콜론(:) 을 사용해서 들여쓰기 하도록 만들었기 때문임.파이썬은 블럭구분을 들여쓰기를 통해 함.
#                 콜론(:) 뒤에 나오는 명령어를 다음줄에 작성하려면 들여쓰기를 해야함.
#     4.2 함수
#       • Len 함수
#         ○ 리스트변수안에 있는 요소들이 몇 개인지 출력하는 함수
#         ○ 단일 변수인 경우는 글자 개수 출력해줌
#         a = ['7839', 'KING', 'PRESIDENT', '0', '1981-11-17', '5000', '', '10']
#                                                               # None(오라클의 null)
#         cnt = len(a)  # none 포함 8개로 인식함
#         print(cnt)
#
#       • def 함수
#         def nvl(a, b):  # nvl이라는 함수를 만든다
#         if a is '':  # a 가 '' 이면
#             return b  # b를 출력한다
#         return a  # else a  출력
#
#       • 오라클과 비교 오라클 & 파이썬
#         ○ 문자함수
#             upper   -> upper()
#             lower   -> lower()
#             initcap -> 사용자 함수
#             substr  -> 변수[1:2]
#             replace -> replace()
#             length  -> len()
#             rtrim   -> rstrip()
#             ltrim   -> lstrip()
#             trim    -> strip()
#             rpad    -> 사용자 함수
#             lpad    -> 사용자 함수
#             instr   -> 사용자 함수
#
#         ○ 숫자함수
#             round   -> round()
#             trunc   -> trunc()
#             mod     -> %
#             power   -> pow
#
#         ○ 날짜함수
#             months_between -> 사용자 함수
#             add_months     -> relativedelta ( 오라클의 sysdate : import datetime 후 today=datetime.date.today() print(today) )
#             next_day       -> 사용자 함수                         또는 from datetime import date 후 print(date.today())
#             last_day       -> monthrange
#                               today().day : 오늘 날짜 일 / today().month : 오늘 날짜 월 / today().year : 오늘 날짜 연도
#                               날짜형 뒤에 day, month, year를 붙이면 필요한 것만 뽑아볼 수 있다.
#
#         ○ 변환함수
#             to_char    -> str()
#             to_number  -> int(), float()
#             to_date    -> datetime.strptime()
#
#         ○ 일반함수
#             nvl       -> 사용자 함수
#             decode    -> 사용자 함수
#             case      -> if 문
#
#         ○ 그룹함수
#             max       -> max
#             min       -> min
#             count     -> count
#             sum       -> sum
#             avg       -> 사용자 함수
#
#
#
#
#
#       • 파이썬의 유용한 함수
#         ○ 문자함수
#             format()
#             isalpha()
#             isnumeric()
#             isspace()
#
#         ○ 변환함수
#             list()
#             tupple()
#
#         ○ 기타(틱택토 코드 이해 위해 필수로 알아야하는 중요 함수)
#             split
#             file = 'a b c d e f g'
#             print(file.split(' '))  # 공백 ' ' 별로 단어를 쪼개라
#
#             append: 추가만 해주고 return 값이 없음
#             a = [1, 2, 3]
#             a.append(4)
#             --> a = [1, 2, 3, 4]
#
#                 b = []
#                 b.append(1)
#                 b.append(2)
#                 b.append(3)
#
#             range
#             count
#             a = 'HELLO'
#             b = a.count('L')  # a 변수에서 1이 몇개 있는가
#             c = ['Anna', 'Elsa', 'Anna', 'Elsa']
#             d = c.count('Elsa')
#             print(d)
#
#     4.3 산술 연산자
#
#       • 산술 연산자: 더하기(+), 빼기(-).....나머지값( %)
#
#       • 오라클과 비교
#         ○ 산술 연산자
#             + - * / (동일)
#             mod -> %
#
#         ○ 비교 연산자
#             =        ->    ==
#             !=       ->   !=
#             >        ->    >
#             <>       ->   <>
#             <=, >=   ->    <=, >=
#
#         ○ 논리 연산자
#             and -> &
#             or  -> |
#             not -> !
#
#         ○ 기타 연산자(오라클 -> 파이썬기본 -> Pandas모듈)
#             between and   ->   <= & >=                  ->   >= & <=
#             in            ->   in                       ->   .isin ( emp['job'].isin )
#             is null       ->   == ''                    ->   .isnull ( emp[job'].isnull() )
#             like          ->   ^, $, 정규식 함수, [0:1]   ->   apply함수 + lambda 표현식
#             ||            ->   +                        ->
#
# 중요! : split을 하고 split을 또 하면 각개가 리스트가 된다!
# 중요! : if 조건에 &로 여러 조건을 주려면 각 조건들을 ()로 꼭 묶어줘야만 한다.(문제62번 참조)
# 중요! : 철자의 마지막 글자는 [-1]이다. 이는 기준커서를 오른쪽에서 시작하는 것을 의미한다. 뒤에서 두번째 글자는 [-2] 이다.
#
# 5장. 데이터 다루기 : 리스트와 튜플과 딕셔너리
#  1. 리스트 변수
#  2. 튜플 변수
#  3. 딕셔너리 변수
#
#    5.1 리스트 변수
#      • 리스트 변수 : 데이터의 목록을 다루는 자료형. [ ] 안에 데이터를 입력해서 관리하는 변수.
#
#      • 리스트 변수의 메소드 함수
#        1. append()  : 리스트 끝에 새 요소를 입력
#        2. extend()  : 기존 리스트에 다른 리스트를 이어 붙임
#        3. insert()  : 리스트의 특정 위치에 새로운 요소를 입력
#        4. remove()  : 리스트의 요소를 제거
#        5. pop()     : 리스트의 마지막 요소를 제거(스택 자료 구조)
#        6. index()   : 리스트의 특정위치의 요소를 출력
#        7. count()   : 리스트의 요소의 건수를 출력
#        8. sort()    : 리스트의 요소를 정렬
#        9. reverse() : 리스트의 요소 순서를 반대로 뒤집음
#
#
#    5.2 튜플 변수
#      • 튜플 변수 : 리스트 변수와 다르게 변경이 불가능한 자료형. ( ) 안에 데이터를 입력해서 관리하는 변수.
#                  변경이 불가능 하므로 튜플로 만든 데이터에 대한 신뢰도가 높아진다.
#
#
# 중요! : Pandas 모듈 사용법
#
#  기본 문법 : 판다스 데이터 프레임 [ 열 ] [ 행 ]
#
# 판다스 데이터 프레임 만드는 문법 : csv 파일을 읽어서 판다스 데이터 프레임을 만든다
#
# 판다스에서 not은 ~ 로 표현한다. (empresult=emp[['ename','sal','job]][~emp['job'].isin(['SALESMAN','ANALYST'])]
# ex)
#     import pandas as pd
#     emp = pd.DataFrame.from_csv("D:/data/emp.csv")
#     empresult = emp[ ['ename','sal']][ emp['sal'] == 3000 ]
#     print (empresult)
#
# Lambda 표현식
# - 여러줄의 코드를 한줄로 만들어주는 인자
#   ex)
#      def hap(x,y)
#         return x + y
#      print(hap(10,20))
#
#      -----------------
#
#      print( (lambda x,y: x + y)(10,20) )
#
# group 함수(max, min, mean, sum, count)를 pandas에서 이용할 때
#  예)
#       emp[ ['sal'] ][emp['job']=='SALESMAN'].max() - 직업이 SALESMAN인 사원 월급 중 최대값 출력
#       emp.groupby('job')['sal'].max()              - 직업별 최대값 출력 : 판다스데이터프레임.groupby[기준컬럼]
#
#
#     5.3 딕셔너리 변수(p.110)
#      • 딕셔너리 변수 : key와 value를 조합해서 사용하는 자료형
#          예) dic = {}
#              dic['파이썬']='www.python.org'
#              dic['구글'] = 'www.google.com'
#              dic['블리자드'] = 'kr.battle.net'
#
#       • 딕셔너리 명령어 : dic.keys() - 키 확인, dic.values() - 값 확인, dic.pop('값') - 값인 요소를 제거, dic.clear() - 전체 다 삭제
#
#
# 6장. if문과 loop문
#  1. if 문
#  2. for loop 문
#  3. while loop 문
#  4. 중첩 loop 문
#  5. continue와 break 사용법
#
#  알고리즘들을 파이썬으로 구현
#
#
#    6.1 if문 (p.126)
#      • if문 구조
#           if 조건1 :   <--- 조건이 True면 실행되고 False면 실행안됨(p.118 참조)
#               실행문         조건문에서 False 로 평가되는 경우 : False, None, 숫자 0, 비어있는 순서열( '', (), [] ), 비어있는 딕셔너리( {} )
#           elif 조건2 :
#               실행문
#           :
#           else:       <--- 생략 가능
#               실행문
#
#    6.2 for loop문 (p.126)
#      • for loop문 구조
#          for i in (리스트, 튜플, 문자열 사용가능):
#              예)
#                 for i in (1,2,3): - 튜플
#                 1
#                 2
#                 3
#
#                 for i in [1.2.3]: - 리스트
#                 1
#                 2
#                 3
#
#         * range : loop 도는 조건 범위를 설정 가능하다. for i in range(1,10,2) 라고 하면 1부터 10까지 루프하는데 2단위로 루프. 1 3 5 7 9가 루프된다.
#
# * mit 공대 머신러닝 코드를 이해하기 위해 알아야 하는 것
#      1. format 함수
#      2. for loop
#      3. 사용자 함수
#      4. 자료형 - 리스트, 튜플, 딕셔너리
#      5. 몬테카를로 알고리즘
#      6. 탐욕 알고리즘
#      7. if 문
#      8. 특정 수학 공식 : self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)
#
#
#
# 6.5 continue와 break 사용법
# -continue : 반복문이 실행되는 동안 특정 코드블럭은 실행하지않고 다른 코드 블럭만 실행되게할때사용하는 문법
#
# for i in range(10):
#     if i % 2 == 1:
#         continue
#
#     print(i)
#
# 0
# 2
# 4
# 6
# 8
#
# = > i % 2 == 1:
# continue: i가 홀수이면 지나가고 짝수만 실행되게 된다
# 문제131 숫자를 1 ~10 을 출력하는데 중간에 5 는 출력되지 않게 출력!
#
# for i in range(1, 11):
#     if i == 5:
#         continue
#
#     print(i)
#
# num = 0
# while num < 10:
#     num += 1
#     if num == 5:
#         continue
#
#     print(num)
#
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
#
# -break문 루프를 중단시키는 역할을 하는 문법
#
# i = 0
# while (True):
#     i += 1
#     if i == 10000000:
#         print('i 가 {0} 이 됬습니다. 반복문 중단!'.format(i))
#         break
#
# print(i)
#
# i가 10000000 이 됬습니다.반복문 중단! 10000000
#

# ※ 6장에서 배운 내용과 if 문과 loop 문을 정리하는 문제
#
# - pandas를 이용해서
# 1. 판다스 기본문법
# 2. 판다스 연산자
# 3. 판다스 이용해서 서브쿼리
# 4. 판다스 이용해서 조인
#
# - pandas를 이용하지 않고 조인
# 1. for loop 문을 중첩해서 문제를 해결
# 2. 딕셔너리 데이터 타입을 이해(MIT 코드에서도 중요하게 쓰인다)

#
#     7장 목차
#
# 1. 함수 생성하는 방법
# 2. 기본값 매개변수와 키워드 매개변수(MIT 코드 이해)
# 3. 가변 매개변수(MIT 코드 이해)
# 4. 매개변수로 함수 사용하는 경우
# 5. 함수 밖의 변수, 함수 안의 변수
# 6. 재귀함수(MIT 코드 이해)
# 7. 중첩 함수
#
# 7.1 함수 생성하는 방법
#
#
# def 함수이름(매개변수):
#     실행문
#
#     return 결과
#
#
# def my_abs(arg):
#     if (arg < 0):
#         result = arg * -1
#     else:
#         result = arg
#
#     return result
#
#
# print(my_abs(-5))
#
#
# 7.4.매개변수로 함수 사용하는 경우
# - 미분 함수 생성
#
#
# def numerical_diff(f, x):
#     delta = 0.0001  # 1e-4 로 해도 된다
#
#
# return (f(x + h) - f(x - h)) / (2 * h)
#
# 함수 f(x) = 2 x ^ 2 + 1 생성
#
#
# def function_1(x):
#     return 2 * pow(x, 2) + 1
#
#
# def numerical_diff(f, x):
#     delta = 0.0001  # 1e-4 로 해도 된다
#     return (f(x + delta) - f(x - delta)) / (2 * delta)
#
#
# def function_1(x):
#     return 2 * pow(x, 2) + 1
#
#
# print(numerical_diff(function_1, -2))
#
# -8.000000000008
#

#
#
# print(numerical_diff(function_1, -2))
#
# -5.000000000006111
#
# - 어순번역 : nested loop join을 구현 - 데이터 양이 많아지면 느려진다. -> hash join으로 구현(해쉬 알고리즘)
#
# 7.2 기본값 매개변수와 키워드 매개변수
#     - 기본값 매개변수 : 입력하지 않으면 기본으로 할당되는 매개변수(p.145)
#                예) 로그함수 log(4,2) , log(10)
#                              밑 지수      지수(밑수는 자연수 e)
#                예제
#                     def print_string(text, count=1):
#                         for i in range(count):
#                             print(text)
#                     print_string("안녕하세요")
#                     print('---------------')
#                     print_string("안녕하세요",2)
# 7.3 가변 매개변수(p.147)
#       문자열.format() 함수 처럼 매개변수의 수가 유동적인 함수를 만들고 싶을 떄 사용하는 변수.
#       함수 실행할 떄 매개변수를 10개, 20개를 입력해도 제대로 동작을 한다.
#       * 파이썬에서 * 이 쓰이는 경우 : 가변 매개변수, 리스트 변수 내의 요소들을 뽑아낼때(mit 코드)
#                                  -> mit 틱틱토 코드의 경우 cells와 *cells 비교
#                                     (cells 는 리스트 변수, *cells는 리스트 변수 내 X, O . print(cells)와 print(*cells)를 꼭 해봐서 차이 비교)
#
#
#
#        def 함수이름(*매개변수):
#            코드블럭
#
#       예제
#           def merge_string(*text_list):
#               result=''
#               for s in text_list:
#               result = result + s + ' '
#               return result
#
#      * 함수의 종료의 의미로 return을 사용하는 경우
#         예제
#             def stop(num):
#                 for i in range(1,num+1):
#                     print('숫자 {0}을 출력합니다'.format(i))
#                     if i = 5:
#                         return   # return 뒤에 아무것도 적지 않으면 함수 종료를 의미한다.
#
#
# 7.5 함수 밖의 변서, 함수 안의 변수
#     - 로컬변수 : 함수 내에서만 사용하는 변수
#     - 글로벌변수 : 함수내,외 둘다 사용가능한 변수. 특정함수에서 출력된 결과를 다른 함수에서 사용할 때 사용.
#
#     함수 안의 변수와 함수 밖의 변수가 서로 이름이 같다고 해도 다른 변수. 같은 변수로 사용하려면 global 변수로 따로 선언해야만 함
#     예제
#          def scope_test():
#                 a=1  #  함수 내에서 사용하는 로컬 변수
#                 print('a : {0}'.format(a))
#          scopt_test()
#
# 7.6 재귀함수
#       - 재귀함수는 함수 내에서 다시 자신을 호출한 후 그 함수가 끝날 때 까지 함수 호출 이후의 명령문이 수행되지 않는다.
#         반복문 + 스택 구조가 결합된 함수
#             * 스택과 큐
#               - 큐 : 자료의 입 출력이 양방향으로 일어나는 것.  A로 들어와서 B로 나간다. 따라서 데이터를 입력한 순서대로 출력한다.
#               - 스택 : 자료의 입 출력이 단방향으로 일어나는 것. A로 들어와서 A로 나간다. 따라서 데이터를 입력한 순서의 반대로 출력한다.
#                 큐의 예 -> SQL 락걸림 현상. 먼저 실행한 계정/쿼리 부터 실행. 첫 실행자가 commit을 해줘야 그 다음차례가 실행 가능하다.

7.7
중첩함수

• 파이썬에서는
함수
안에
함수를
정의할
수
있다.
• 중첩함수는
자신이
소속된
함수의
매개변수에
접근
가능

• 예제: 표준편차
평균값
구하는
함수
분산
구하는
함수
제곱근
구하는
함수
가
필요함


def stddev(*args):
    import math

    def mean():  # 평균 함수
        return sum(args) / len(args)

    def variance(m):  # 분산 함수
        total = 0
        for arg in args:
            total += (arg - m) ** 2
        return total / (len(args) - 1)

    v = variance(mean())
    return math.sqrt(v)


stddev(2.3, 1.7, 1.4, 0.7, 1.9)
• 재귀
알고리즘
완성하는
문제
○ mit
코드를
이해히기
위해
반드시
알아야
하는
알고리즘
§ greedy
알고리즘
당장
눈
앞의
이익만
추구하는
것
먼
미래를
내다
보지
않고
지금
당장의
최선이
무엇인가만
판단

• 문제156.가변
매개변수를
이용해서
여러개의
숫자를
입력받아
중첩함수로
최대공약수
출력.


def manygong(*args):
    list_gong = []
    for arg in args:
        list_gong.append(arg)

    def gcdtwo(a, b):
        if min(a, b) == 0:
            return max(a, b)
        return gcdtwo(b, a % b)

    def gcd(a):
        b = gcdtwo(max(a), min(a))
        a.remove(min(a))
        a.remove(max(a))
        a.append(b)

        if max(a) == min(a):
            print('최대공약수는 : ', a[0])
        else:
            gcd(a)

    return gcd(list_gong)


8
장.모듈과
패키지

1.
모듈이란?
2.
import 사용법

3.
모듈
찾는
방법
4.
메인
모듈과
하위
모듈
5.
패키지
6.
_ini_.py

8.1
모듈이란?

• 모듈: 독자적인
기능을
갖는
구성요소.파이썬에서는
각각의
소스
파일을
일컬어
모듈이라고
한다.
• 모듈
예


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def muliply(a, b):
    return a * b


def divide(a, b):
    return a / b


calculator.py
라는
이름으로
저장.new
버튼
눌러서
새
창
열고
아래
내용
코딩
후
아까
저장한
위치와
같은
위치에
calc_tester.py
라는
이름으로
저장

import calculator

print(calculator.plus(10, 5))

8.2
import 사용법

• import 의

역할은
다른
모듈
내의
코드에
접근
가능하게
하는
것
• import 가

접근
하도록
해주는
코드에는
변수, 함수, 클래스
등이
모두
포함
• 앞에서
썼던
문법
import 모듈명

import calculator

print(calculator.plus(10, 5))

• 좀더
편하게
코딩하는
문법
from 모듈명 import 변수

또는
함수

from calculator import plus
from calculator import minus

print(plus(10, 5))

• 더
편하게
코딩하는
문법: but
사용하지
않는게
좋음.코드
복잡.모듈
수가
많아지면
어떤
모듈, 어떤
함수
불러오는지
파악이
어려워짐
from calculator import *

print(plus(10, 5))

• 타협
방법
import calculator as c

print(c.plus(10, 5))

• 모듈
불러올
때
특정
문장
실행
안
되게
하는
방법
if__name__ == "__main__":  # 모듈 불러올 때 이 문장 이후의 문장은 수행되지 x

○ mit
코드의
실제
사용예
if __name__ == "__main__":
        p1 = Agent(1, lossval=-1)
    p2 = Agent(2, lossval=-1)
  
    for i in range(10000):
            if i % 10 == 0:
                    print('Game: {0}'.format(i))
    
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)
 
    while True:
            p2.verbose = True
        p1 = Human(1)
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

8.3
모듈
찾는
방법

• 방금
만든
calculator
모듈의
위치는
우리가
직접
지정한
위치에
저장되어
있었고, calc_test.py
에서
calculator
모듈을
불러올
수
있었음

• sys
라는
모듈(예: random
함수를
포함하고
있는
모듈)은
어디에
있는가?

• 파이썬은
import 수행시

다음
순서로
모듈
파일
찾음
○ 파이썬
인터프리터
내장
모듈
○ sys.path
에
정의
되어
있는
디렉토리

• sys
모듈은
파이썬의
내장
모듈.sys
모듈에
뭐
있는지
확인하는
코드
import sys

print(sys.builtin_module_names)

• sys.path
의
내용을
출력해서
파이썬이
어떻게
모듈
탐색해
나가는지
확인
import sys

for path in sys.path:
    print(path)









• 문제160.표준편차를
출력하는
함수를
모듈화
시켜서
다른
실행창에서
실행


def stddev(*args):
    import math

    def avg():
        return sum(args) / len(args)

    def variance(a):
        total = 0
        for arg in args:
            total += (arg - a) ** 2
        return total / (len(args) - 1)

    return math.sqrt(variance(avg()))


if __name__ == "__main__":
    print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))

import stddev as st

st.stddev(2.3, 1.7, 1.4, 0.7, 1.9)
• 문제161.
