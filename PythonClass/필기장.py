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
#
# 7.7 중첩함수
#
# • 파이썬에서는 함수 안에 함수를 정의할 수 있다.
# • 중첩함수는 자신이 소속된 함수의 매개변수에 접근 가능
#
# • 예제: 표준편차 평균값 구하는 함수 분산 구하는 함수 제곱근 구하는 함수 가 필요함
#
#
# def stddev(*args):
#     import math
#
#     def mean():  # 평균 함수
#         return sum(args) / len(args)
#
#     def variance(m):  # 분산 함수
#         total = 0
#         for arg in args:
#             total += (arg - m) ** 2
#         return total / (len(args) - 1)
#
#     v = variance(mean())
#     return math.sqrt(v)
#
#
# stddev(2.3, 1.7, 1.4, 0.7, 1.9)
# • 재귀 알고리즘 완성하는 문제
# ○ mit 코드를 이해히기 위해 반드시 알아야 하는 알고리즘
# § greedy 알고리즘 당장 눈 앞의 이익만 추구하는 것 먼 미래를 내다 보지 않고 지금 당장의 최선이 무엇인가만 판단
#
# • 문제156.가변 매개변수를 이용해서 여러개의 숫자를 입력받아 중첩함수로 최대공약수 출력.
#
#
# def manygong(*args):
#     list_gong = []
#     for arg in args:
#         list_gong.append(arg)
#
#     def gcdtwo(a, b):
#         if min(a, b) == 0:
#             return max(a, b)
#         return gcdtwo(b, a % b)
#
#     def gcd(a):
#         b = gcdtwo(max(a), min(a))
#         a.remove(min(a))
#         a.remove(max(a))
#         a.append(b)
#
#         if max(a) == min(a):
#             print('최대공약수는 : ', a[0])
#         else:
#             gcd(a)
#
#     return gcd(list_gong)
#
#
# 8장.모듈과 패키지
#
# 1. 모듈이란?
# 2. import 사용법
# 3. 모듈 찾는 방법
# 4. 메인 모듈과 하위 모듈
# 5. 패키지
# 6. _init_.py
#
# 8.1 모듈이란?
#
# • 모듈: 독자적인 기능을 갖는 구성요소.파이썬에서는 각각의 소스 파일을 일컬어 모듈이라고 한다.
# • 모듈 예
#
# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def muliply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# calculator.py 라는 이름으로 저장.new 버튼 눌러서 새 창 열고 아래 내용 코딩 후 아까 저장한 위치와 같은 위치에 calc_tester.py 라는 이름으로 저장
#
# import calculator
#
# print(calculator.plus(10, 5))
#
# 8.2 import 사용법
#
# • import 의  역할은 다른 모듈 내의 코드에 접근 가능하게 하는 것
# • import 가 접근 하도록 해주는 코드에는 변수, 함수, 클래스 등이 모두 포함
# • 앞에서 썼던 문법
# import 모듈명
#
# import calculator
#
# print(calculator.plus(10, 5))
#
# • 좀더 편하게 코딩하는 문법
# from 모듈명 import 변수
#
# 또는 함수
#
# from calculator import plus
# from calculator import minus
#
# print(plus(10, 5))
#
# • 더 편하게 코딩하는 문법: but 사용하지 않는게 좋음.코드 복잡.모듈 수가 많아지면 어떤 모듈, 어떤 함수 불러오는지 파악이 어려워짐
# from calculator import *
#
# print(plus(10, 5))
#
# • 타협 방법
# import calculator as c
#
# print(c.plus(10, 5))
#
# • 모듈 불러올 때 특정 문장 실행 안 되게 하는 방법
# if__name__ == "__main__":  # 모듈 불러올 때 이 문장 이후의 문장은 수행되지 x
#
# ○ mit 코드의 실제 사용예
# if __name__ == "__main__":
#         p1 = Agent(1, lossval=-1)
#     p2 = Agent(2, lossval=-1)
#   
#     for i in range(10000):
#             if i % 10 == 0:
#                     print('Game: {0}'.format(i))
#     
#         winner = play(p1, p2)
#         p1.episode_over(winner)
#         p2.episode_over(winner)
#  
#     while True:
#             p2.verbose = True
#         p1 = Human(1)
#         winner = play(p1, p2)
#         p1.episode_over(winner)
#         p2.episode_over(winner)
#
# 8.3 모듈 찾는 방법
#
# • 방금 만든 calculator 모듈의 위치는 우리가 직접 지정한 위치에 저장되어 있었고, calc_test.py 에서 calculator 모듈을 불러올 수 있었음
#
# • sys 라는 모듈(예: random 함수를 포함하고 있는 모듈)은 어디에 있는가?
# • 파이썬은 import 수행시 다음 순서로 모듈 파일 찾음
# ○ 파이썬 인터프리터 내장 모듈
# ○ sys.path 에 정의 되어 있는 디렉토리
#
# • sys 모듈은 파이썬의 내장 모듈.sys 모듈에 뭐 있는지 확인하는 코드
# import sys
#
# print(sys.builtin_module_names)
#
# • sys.path 의 내용을 출력해서 파이썬이 어떻게 모듈 탐색해 나가는지 확인
# import sys
#
# for path in sys.path:
#     print(path)
#
#
# 8장.모듈과 패키지
# 1. 모듈이란?
# 2. import 사용법
# 3. 모듈 찾는 방법
# 4. 메인 모듈과 하위 모듈
# 5. 패키지
# 6. _init_.py
# 7. site - package
#
# 8.1 모듈이란?
#
# • 모듈: 독자적인 기능을 갖는 구성요소.파이썬에서는 각각의 소스 파일을 일컬어 모듈이라고 한다.
# • 모듈 예
#
#
# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def muliply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# calculator.py 라는 이름으로 저장.new 버튼 눌러서 새 창 열고 아래 내용 코딩 후 아까 저장한 위치와 같은 위치에 calc_tester.py 라는 이름으로 저장
#
# import calculator
#
# print(calculator.plus(10, 5))
#
# 8.2import 사용법
#
# • import 의 역할은 다른 모듈 내의 코드에 접근 가능하게 하는 것
# • import 가 접근 하도록 해주는 코드에는 변수, 함수, 클래스 등이 모두 포함
# • 앞에서 썼던 문법
#
# import 모듈명
#
# import calculator
#
# print(calculator.plus(10, 5))
#
# • 좀더 편하게 코딩하는 문법 from 모듈명 import 변수
#
# 또는 함수
#
# from calculator import plus
# from calculator import minus
#
# print(plus(10, 5))
#
# • 더 편하게 코딩하는 문법: but 사용하지 않는게 좋음.코드 복잡.모듈 수가 많아지면 어떤 모듈, 어떤 함수 불러오는지 파악이 어려워짐
# from calculator import *
#
# print(plus(10, 5))
#
# • 타협 방법
# import calculator as c
#
# print(c.plus(10, 5))
#
# • 모듈 불러올 때 특정 문장 실행 안 되게 하는 방법
# if __name__ == "__main__":  # 모듈 불러올 때 이 문장 이후의 문장은 수행되지 x
#
# ○ mit 코드의 실제 사용예
# if __name__ == "__main__":
#         p1 = Agent(1, lossval=-1)
#     p2 = Agent(2, lossval=-1)
#   
#     for i in range(10000):
#             if i % 10 == 0:
#                     print ('Game: {0}'.format(i))
#     
#         winner = play(p1, p2)
#         p1.episode_over(winner)
#         p2.episode_over(winner)
#  
#     while True:
#             p2.verbose = True
#         p1 = Human(1)
#         winner = play(p1, p2)
#         p1.episode_over(winner)
#         p2.episode_over(winner)
#
# 8.3 모듈 찾는 방법
#
# • 방금 만든 calculator 모듈의 위치는 우리가 직접 지정한 위치에 저장되어 있었고, calc_test.py 에서 calculator 모듈을 불러올 수 있었음
#
# • sys 라는 모듈(예: random 함수를 포함하고 있는 모듈)은 어디에 있는가?
# • 파이썬은 import 수행시 다음 순서로 모듈 파일 찾음
# ○ 파이썬 인터프리터 내장 모듈
# ○ sys.path 에 정의 되어 있는 디렉토리
#
# • sys 모듈은 파이썬의 내장 모듈.sys 모듈에 뭐 있는지 확인하는 코드
# import sys
#
# print(sys.builtin_module_names)
#
# • sys.path 의 내용을 출력해서 파이썬이 어떻게 모듈 탐색해 나가는지 확인
# import sys
#
# for path in sys.path:
#     print(path)
#
# 8.4 메인 모듈과 하위 모듈
# • 파이썬 문법 + 중요한 알고리즘 20 가지는 외워버려야 함
#
# • 코드를 어떻게 만드는가 ?  함수 생성 후 모아 놓은 모듈
# • 코드를 어떻게 실행하는가 ?  메인 모듈(최상위 수준으로 실행되는 스크립트)
#
# • _name_ 변수: 내장 전역변수.이를 이용해 지금 쓰는 모듈이 메인 모듈인지, 하위 모듈인지 확인 가능
# ○ 메인 모듈: _name_ - --> main 이라고 나옴
# ○ 하위 모듈: _name_ - --> 모듈명으로 나옴
# ○ 예제1 print(' name : {0} '.format(__name__)) 을 top_level.py 라는 이름으로 저장
# ○ 예제2 print("begining of sub.py....") print('name : {0}'.format(__name__)) print("end of sub.py ...") 을 sub.py 라는 이름으로 저장하고 실행
# ○ 예제3 import sub print("begining of test7.py....") print('name : {0}'.format(__name__)) print("end of test7.py ...") 을 test7.py 라는 이름으로 저장하고 실행
#
# 실행결과
# begining of sub.py....  # import sub 했더니 sub.py 의 print 부분이  출력되어 나온 것
# name: sub
# end of sub.py...
#
# begining of
# sub.py....  # test7 에 있는 부분이 출력
# name: __main__
# end of sub.py...
#
# 8.5패키지
#
# • 패키지: 모듈을 모아놓은 디렉토리
# • 모듈: 실행할 함수들을 모아놓은 스크립트
#
# • 평범한 디렉토리가 파이썬의 패키지로 인정 받으려면, __init__.py 라는 파일이 디렉토리 안에 있어야 함.
#
# ○ 두 모듈 저장하기
# __init__.py: 비어있는 문서
# calculator.py: 모듈
#
# ○ cal_test7.py 스크립트를 __init__.py 와 calculator.py 가 저장된 폴더보다 한 수준위의 폴더에 만든다.
#
# from Administrator import calculator  # from (init 과 calculator.py 저장된 폴더명)  import 모듈
#
# print(calculator.plus(10, 5))
# print(calculator.minus(10, 5))
#
# 8.6 __init__.py
#
# • __init__.py는 보통 비워둠.__all__ 이라는 변수 조정할때만 건드림.
# • __all__ 변수: 패키지로부터 반입할 모듈의 목록을 정의하기 위해 사용
# ○ from 패키지 import * 에서 * 이 뜻하는 모든 모듈이 뭐가 있는지 파이썬이 알려면 __init__.py 의 __all__ 변수에 아래와 같이 명시 해줘야 함.
# ○ __all__ = ['plus_module', 'minus_module', 'multiply_module', 'divide_module'] 이라는 문구를 써주면 됨.
#
# • 예제
# ○ C:\Users\Administrator\python 폴더에 4 개의 모듈을 만들어서 저장
# § plus_module.py
# § minus_module.py
# § multiply_module.py
# § divide_module.py
# ○ __init__.py내에 __all__ = ['plus_module', 'minus_module', 'multiply_module', 'divide_module'] 쓰고 저장
# ○ cal_test7 에서
#
# from python import *
# print(plus_module.plus(10, 5)) 해보기
#
# 8.7 site - package에 대해
# • site
# ○ package란 파이썬의 기본 라이브러리 패키지 외에 추가적인 패키지를 설치하는 디렉토리
# ○ package 디렉토리에 여러 소프트웨어가 사용할 공통 모듈을 넣어두면 물리적 장소에 구애받지 않고 모듈에 접근하여 반입 가능
#
# • site위치 확인하는 법
# import sys
#
# print(sys.path)
#
# • 폴더옮기기 기존의 모듈 폴더 내용을 전주 site_package에 복사
#
# • 문제160.표준편차를 출력하는 함수를 모듈화 시켜서 다른 실행창에서 실행
#
#
# def stddev(*args):
#     import math
#
#     def avg():
#         return sum(args) / len(args)
#
#     def variance(a):
#         total = 0
#         for arg in args:
#             total += (arg - a) ** 2
#         return total / (len(args) - 1)
#
#     return math.sqrt(variance(avg()))
#
#
# if __name__ == "__main__":
#     print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))
#
# import stddev as st
#
# st.stddev(2.3, 1.7, 1.4, 0.7, 1.9)
#
# • 문제162.위import sub 만으로도 아래 내용이 출력 되었는데, 출력 안 되게 하려면 어떻게 해야 하나
# import sub
#
# print("begining of test7.py....")
# print('name : {0}'.format(__name__))
# print("end of test7.py ...")
# 을 test7.py 라는 이름으로 저장하고 실행
#
# 실행결과
#
# begining of sub.py....  # import sub 했더니 sub.py 의 print 부분이  출력되어 나온 것 name: sub end of sub.py...
# begining of sub.py....  # test7 에 있는 부분이 출력
# name: __main__end of sub.py...
#
# if __name__ == "__main__":
#     print("begining of sub.py....")
#     print('name : {0}'.format(__name__))
#     print("end of sub.py ...")
#     라고 sub.py를 바꿔주면 안 나옴
#
# • 문제163.d:\my_loc2라는 디렉토리 만들고 cal_test.py 스크립트 가져다 두고 실행
#
# 9장.객체와 클래스(중요)
#
# 1. 객체와 클래스
# 2. 클래스의 정의
# 3. __init__() 메소드를 이용한 초기화
# 4. self 에 대해
# 5. 정적 메소드와 클래스 메소드
# 6. 클래스 내부에게만 열려있는 프라이빗 멤버
# 7. 상속
# 8. 오버라이딩
# 9. __call() __메소드
# 10. for 문으로 순회를 할 수 있는 객체 만들기
# 11. 추상기반 클래스
#
# 9.1 객체와 클래스
#
# • 객체(object) = 속성(attribute) + 기능
# 자동차 색깔, 바퀴 크기 전진, 후진
# 객체 = 변수 + 함수
#
# • 예제
#
#
# class car:
#     # 속성을 나타내는 변수들
#     def __init__(self):  # 초기화해주는 함수
#         self.color = 0xFF000  # 자동차 색깔
#         self.wheel_size = 16  # 바퀴 크기
#         self.displacement = 2000  # 엔진 배기량
#
#     # 전진하는 기능
#     def forward(self):
#         pass
#
#     # 후진하는 기능
#     def backward(self):
#         pass
#
#     # 좌회전
#     def turn_left(self):
#         pass
#
#     # 우회전
#     def turn_right(self);
#
#     pass
#
#
# # 메인모듈일 때 아래 스크립트 실행
# if __name__ == '__main__':
#     # 클래스를 가지고 인스턴화 하는 코드
#     my_car = car()  # car() 클래스로 my_car라는 객체를 생성 . 이전까지는 class car는 자료형임.
#
#     # my_car 에 대한  정보 출력
#     print('0x{:02X}'.format(my_car.color))
#     print(my_car.wheel_size)
#     print(my_car.displacement)
#
#     # my_car의 메소드 호출
#     my_car.forward()
#     my_car.backward()
#     my_car.turn_left()
#     my_car.turn_right()
#
# ○ __init__: 객체 생성될 때 호출되는 메소드로, 객체 초기화 담당
# ○ self: 메소드의 첫번재 매개변수로 객체 자신을 나타냄.
# ○ my_car = car(): car()
# 생성자는 car 클래스의 인스턴스를 생성하여 반환함.(my_car - --> 인스턴스(실체), car() - --> 생성자(설계도) )
#
#
# 9.2 클래스의 정의
#
# • 클래스(자료형) - --> 객체(변수)
# 붕어빵틀 붕어빵(인스턴스화 됨 or 실체화 됨)
# • 객체: 속성(붕어빵 색, 앙금) + 기능(오른쪽 왼쪽으로 움직이는 것)
#
#
#
# 9.3 __init__() 메소드를 이용한 초기화
#
# • 클래스의 생성자가 호출 되면 내부적으로 두 개의 메소드가 호출됨.
# ○ __new__(): 클래스의 실체(인스턴스) 를 만드는 역할.자동으로 호출됨(명시해주지 않아도 됨).
# ○ __init__(): 객체 생성될 때 객체를 초기화하는 역할
#
# • 클래스 생성할 때 __init__() 지정하지 않는다면... ○ 지정 x
#
#
# class ClassVar:
#     text_list = []  # 클래스의 정의 시점에서 바로 메모리에 할당됨
#
#     def add(self, text):
#         self.text_list.append(text)
#
#     def print_list(self):
#         print(self.text_list)
#
#
# if __name__ == '__main__':
#     a = ClassVar()  # 위에서 만든 생성자를 이용해 a라는 실체를 만든다.
#     a.add('a')  # a 라는 객체의 add 기능을 작동
#     a.print_list()  # a 라는 객체의 print_list 기능을 작동
#
#     b = ClassVar()  # 위에서 만든 생성자를 이용해 b라는 객체를 만든다.
#     b.add('b')  # b 객체에 b를 넣는다.
#     b.print_list()  # 출력 결과는 ['a'],   ['a','b'] 가 나옴 why? 초기화하지 않아서 text_list 에 'a' 들어간 상태에서 'b' 가 들어가서 a, b 둘다 나옴
# ○ 지정
# o
#
#
# class ClassVar:
#     def __init__(self):
#         self.text_list = []  # 클래스의 정의 시점에서 바로 메모리에 할당됨
#
#     def add(self, text):
#         self.text_list.append(text)
#
#     def print_list(self):
#         print(self.text_list)
#
#
# if __name__ == '__main__':
#     a = ClassVar()  # 위에서 만든 생성자를 이용해 a라는 실체를 만든다.
#     a.add('a')  # a 라는 객체의 add 기능을 작동
#     a.print_list()  # a 라는 객체의 print_list 기능을 작동
#
#     b = ClassVar()  # 위에서 만든 생성자를 이용해 b라는 객체를 만든다.
#     b.add('b')  # b 객체에 b를 넣는다.
#     b.print_list()  # 출력 결과는 ['a'],   ['a','b'] 가 나옴 why? 초기화하지 않아서 text_list 에 'a' 들어간 상태에서 'b' 가 들어가서 a, b 둘다 나옴
#
# 9.4 self
#
# • self: self는 클래스에서 사용하는 최초 매개변수이며 자기 자신을 가리킴.
#
# • 예제
#
#
# class instanceVar:
#     def __init__(self):  # 자기자신을 초기화
#         text_list = []  # text_list = []
#
#     def add(self, text):  # 자기자신의 text_list 변수를 가리킴
#         self.text_list.append(text)
#
#     def print_list(self):  # 자기자신의 text_list 변수를 가리킴
#         print(self.text_list)
#
#
# 9.5 정적 메소드와 클래스 메소드
#
# • 인스턴스 메소드: 로봇의 팔이 잘 작동하는지 로봇을 만들어놓고 작동해 보며 확인하는 메소드
# ○ 예제 my_car.forward  # 전진해라 실체화(인스턴스)
# • 클래스(정적) 메소드: 로봇의 팔이 잘 작동하는지를 로봇을 만들지 않고 프로그램 코드를 실행시켜 확인하는 메소드
# ○ 필요성
# § 클래스 내 특정 기능 실행할 때 반드시 인스턴스가 생성될 필요가 없는 경우 (실제 로봇 작동 중에는 작동하지 않는 기능)
# § 인스턴스가 생성되지 않은 상태에서 메소드를 호출하고 싶은 경우 (로봇이 만들어지지 않은 상태에서 기능 테스트)
#
# ○ 예제
#
#
# class Calculator:  # 객체 = 속성 + 기능, 기능만 4가지 있는 클래스
#     @staticmethod  # 정적 메소드 선언할 때 사용해야하는 데코레이터
#     def plus(a, b):
#         return a + b
#
#     @staticmethod
#     def minus(a, b):
#         return a - b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#     @staticmethod
#     def divide(a, b):
#         return a / b
#
#
# if __name__ == '__main__':
#     print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7, 4)))  # 정적 메소드 호출하는 방법
#     print("{0} - {1} = {2}".format(7, 4, Calculator.minus(7, 4)))  # 클래스를 통해서 메소드 호출
#     print("{0} * {1} = {2}".format(7, 4, Calculator.multiply(7, 4)))
#     print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7, 4)))
#
#
# • 문제164.책 192 쪽을 보고 초기화하는 코드 추가해서['a'], ['b'] 나오게 하기
#
#
# class ClassVar:
#     def __init__(self):
#         self.text_list = []  # 클래스의 정의 시점에서 바로 메모리에 할당됨
#
#     def add(self, text):
#         self.text_list.append(text)
#
#     def print_list(self):
#         print(self.text_list)
#
#
# if __name__ == '__main__':
#     a = ClassVar()  # 위에서 만든 생성자를 이용해 a라는 실체를 만든다.
#     a.add('a')  # a 라는 객체의 add 기능을 작동
#     a.print_list()  # a 라는 객체의 print_list 기능을 작동
#
#     b = ClassVar()  # 위에서 만든 생성자를 이용해 b라는 객체를 만든다.
#     b.add('b')  # b 객체에 b를 넣는다.
#     b.print_list()  # 출력 결과는 ['a'],   ['a','b'] 가 나옴 why? 초기화하지 않아서 text_list 에 'a' 들어간 상태에서 'b' 가 들어가서 a, b 둘다 나옴
#
#
# • 문제165.머신러닝 코드 입히기 전인 핑퐁 게임을 파이썬으로 구현
# from tkinter import *
# import random
# import time
#
#
# class Ball:
#
#     def __init__(self, canvas, paddle, color):
#             self.canvas = canvas
#
#         self.paddle = paddle
#         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # 공 좌표 및 색깔(oval : object 형태 타입)
#         self.canvas.move(self.id, 245, 100)  # 공을 캔버스 중앙으로 이동
#         starts = [-3, -2, -1, 1, 2, 3]
#         random.shuffle(starts)
#
#          # 공의 속도
#         self.x = starts[0]
#         self.y = -3
#         self.canvas_height = self.canvas.winfo_height()
#         self.canvas_width = self.canvas.winfo_width()
#         self.hit_bottom = False
#
#     def hit_paddle(self, pos):
#             paddle_pos = self.canvas.coords(self.paddle.id)
#
#         if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
#                 if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
#                         return True
#         return False
#
#     def draw(self):
#             self.canvas.move(self.id, self.x, self.y)  # 공을 움직이게 하는 부분
#
#          # 공이 화면 밖으로 나가지 않게 해준다
#         pos = self.canvas.coords(self.id)
#         if pos[1] <= 0:
#                 self.y = 3
#         if pos[3] >= self.canvas_height:  # 바닥에 부딪히면 게임오버
#                 self.hit_bottom = True
#         if pos[0] <= 0:
#                 self.x = 3
#         if pos[2] >= self.canvas_width:
#                 self.x = -3
#         if self.hit_paddle(pos) == True:  # 판에 부딪히면 위로 튕겨올라가게
#                 self.y = -3
#
#
# class Paddle:
#
#     def __init__(self, canvas, color):
#             self.canvas = canvas
#
#         self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
#         self.canvas.move(self.id, 200, 300)
#         self.x = 0
#         self.canvas_width = self.canvas.winfo_width()
#         self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
#         self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
#
#     def draw(self):
#             self.canvas.move(self.id, self.x, 0)
#
#         pos = self.canvas.coords(self.id)
#         if pos[0] <= 0:
#                 self.x = 0
#         elif pos[2] >= self.canvas_width:
#             self.x = 0
#
#     def turn_left(self, evt):
#             self.x = -2
#
#     def turn_right(self, evt):
#             self.x = 2
#
#
# tk = Tk()
# tk.title("Game")
# tk.resizable(0, 0)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()
# paddle = Paddle(canvas, 'blue')
# ball = Ball(canvas, paddle, 'red')
# start = False
# # 공을 약간 움직이고 새로운 위치로 화면을 다시 그리며, 잠깐 잠들었다가 다시 시작해라!
# while 1:
#         if ball.hit_bottom == False:
#                 ball.draw()
#         paddle.draw()
#      # 그림을 다시 그려라! 라고 쉴새없이 명령
#     tk.update_idletasks()
#     tk.update()
#      # 시작 전 2초간 sleep
#     if not start:
#             time.sleep(2)
#         start = True
#     time.sleep(0.01)
#
#
# • 문제165.
#
# 9.6 클래스 내부에게만 열려있는 프라이빗 멤버
#
# - 파이썬에서 사용하느 멤버 2 가지
#
# 1. public member
#
# 클래스 안에서든 밖에서든 접근 가능한 멤버
#
# 예: 접두사가 두개의 밑줄이고 접미사도 두개의 밑줄
#
# __number__
#
# 2. private member
#
# 클래스 안에서만 접근 가능한 멤버 클래스의 사생활을 지켜줘야할때 요긴하게 사용
#
# 예: 접두사가 두개의 밑줄이고 접미사는 없거나 하나의 밑줄
#
# __number __number_
#
# - 퍼블릭 멤버 사용 경우
#
# class YourClass:
#     pass
#
#
# class MyClass:
#     def __init__(self):
#         self.message = 'Hello'
#
#     def some_method(self):
#         print(self.message)
#
#
# obj = MyClass()
#
# obj.some_method()  # 메소드를 실행했기 때문에 출력
# print(obj.message)  # message 라는 변수의 내용 출력
#
# - 프라이빗 멤버 사용 경우
#
# class YourClass:
#     pass
#
#
# class MyClass:
#     def __init__(self):
#         self.message = 'Hello'
#         self.__private = 'private'
#
#     def some_method(self):
#         print(self.message)
#         print(self.__private)
#
#
# obj = MyClass()
#
# obj.some_method()  # 메소드를 실행했기 때문에 출력
# print(obj.message)  # message 라는 변수의 내용 출력
# print(obj.__pivate)  # 프라이빗 멤버는 접근 불가여서 에러
#
# Traceback(most recent call last): File
# "D:/python/source/classs/testing.py", line
# 17, in < module >
# print(obj.__pivate)
# Hello
# AttributeError: 'MyClass'
# object
# has
# no
# attribute
# '__pivate'
# private
# Hello
#
# obj.some_method()  # 메소드를 실행했기 때문에 출력
#
# Hello
# private
#
# print(obj.message)  # message 라는 변수의 내용 출력
#
# Hello
#
# 9.7 상속
#
# 클래스들끼리 유산(기능) 을 물려주는 것
#
# 클래스 - ----------------------------->     클래스
#
# 부모 - ----------------------------->      자식
#
# 으로 물려주는것 유산(기능) 상속을 받게되면 부모의 기능을 굳이 자식 클래스에 코딩하지 않아도 된다
#
# 학습시키는
#
# 클래스(짝꿍) - ------------->     핑퐁게임
# 클래스(나)
#
# 머신러닝 기능 유산 상속
#
# - 예제
#
#
# class Father:
#     def base_methon(self):
#         print("Hello~~")
#
#
# class Child(Father):
#     pass
#
#
# father = Father()
# child = Child()
#
# father.base_methon()
# child.base_methon()
#
# Hello
# ~~
# Hello
# ~~
#
# - __init__ 메소드를 가지고 실행하는데 부모와는 다르게 자식에 message 라는 속성이 없어서 상속 시키고 싶을때
#
#
# class Father:
#     def __init__(self):
#         print("Hello~~")
#         self.message = 'Good Morning'
#
#
# class Child(Father):
#     def __init__(self):
#         Father.__init__(self)  # 이 부분을 해야 child.message 출력
#         print('Hello~~ I am Child')
#
#
# father = Father()
# child = Child()
#
# print(father.message)
# print(child.message)
#
# Hello
# ~~
# Hello
# ~~
# Hello
# ~~ I
# am
# Child
# Good
# Morning
# Good
# Morning
#
# = > 프로그래머가 명시적으로 클래스의 초기화 메소드를 호출해주기를 원한다
#
# super() 는 부모 클래스의 객체역할을 하는 내장 함수 사실상
# super() 함수의 반환값을 상위 클래스의 객체로 간주하고 코딩해도 된다
#
#
# class Father:
#     def __init__(self):
#         print("Hello~~")
#         self.message = 'Good Morning'
#
#
# class Child(Father):
#     def __init__(self):
#         # Father.__init__(self)   # 이 부분을 해야 child.message 출력
#         super().__init__()
#         print('Hello~~ I am Child')
#
#
# father = Father()
# child = Child()
#
# print(father.message)
# print(child.message)
#
# Hello
# ~~
# Hello
# ~~
# Hello
# ~~ I
# am
# Child
# Good
# Morning
# Good
# Morning
#
# - 다중 상속
#
# 두개 이상의 클래스를 상속받는것을 말한다
# 이 경우에는 두 클래스의 모든 속성을 물려받게 된다
#
# 이는 하나의 자식 클래스가 두개 이상의 부모 클래스를 가지는 것이라고 할 수 있다
#
# father1          father2
#  ↘                   ↙
#          child
#
# 예제
#
#
# class Father1:
#     def func(self):
#         print('지식')
#
#
# class Father2:
#     def func(self):
#         print('지혜')
#
#
# class Child(Father1, Father2):
#     def childfunc(self):
#         Father1.func(self)
#         Father2.func(self)
#
#
# objectchild = Child()
# objectchild.childfunc()
#
# 지식
# 지혜
#
# - 그런데 둘다 출력하기 싫고 하나만 출력하고 싶어서 func만 따로 실행하면?
#
# class Father1:
#     def func(self):
#         print('지식')
#
#
# class Father2:
#     def func(self):
#         print('지혜')
#
#
# class Child(Father1, Father2):
#     def childfunc(self):
#         Father1.func(self)
#         Father2.func(self)
#
#
# objectchild = Child()
# objectchild.func()
#
# 지식
#
# = > Father1, Father2가 func로 같은데 Father1.func(self) 를 먼저 했기때문에 지식이 출력!
# = > 우리가 상속받을 클래스의 이름을 나열할때 순서에 따라 이름을 찾기 때문에 이 순서도 중요하다!
#
# - 다중 상속시 주의할점
# 다이아몬드 상속
#
#        Grandfather
#    ↙                 ↘
# Father1            Father2
#    ↘                   ↙
#
#         Grandchild
#
# 예제
#
#
# class GrandFather:
#     def __init__(self):
#         print('튼튼한 두 팔')
#
#
# class Father1(GrandFather):
#     def __init__(self):
#         GrandFather.__init__(self)
#         print('지식')
#
#
# class Father2(GrandFather):
#     def __init__(self):
#         GrandFather.__init__(self)
#         print('지혜')
#
#
# class GrandChild(Father1, Father2):
#     def __init__(self):
#         Father1.__init__(self)
#         Father2.__init__(self)
#         print('자기 만족도가 높은 삶')
#
#
# grandchild = GrandChild()
#
# 튼튼한 두 팔 지식 튼튼한 두 팔 지혜 자기 만족도가 높은 삶
# = > 다이아몬드 상속을 받았더니 그만 팔이 4 개가 되었다
#
# 문제166(점심시간 문제) 다시 팔이 2 개가 되게하시오!
#
# class GrandFather:
#     def __init__(self):
#         print('튼두팔')
# class Father1(GrandFather):
#     def __init__(self):
#         super().__init__()
#         print('지식')
# class Father2(GrandFather):
#     def __init__(self):
#         super().__init__()
#         print('지혜')
# class GrandChild(Father1, Father2):
#     def __init__(self):
#         super().__init__()
#         print('좋은삶')
# gc = GrandChild()
#
# 9.8 오버라이딩
#
# • ~ 보다 우선한다는 뜻.부모로부터 상속받은 메소드를 다시 override(재정의) 하겠다.
#
# • 예제
#
#
# class grandfather:
#     def __init__(self):
#         print("튼튼한 두팔")
#
#
# class father2(grandfather):
#     def __init__(self):
#         print("지혜")
#
#
# arg_father2 = father2()  # 지혜만 나온 이유는 오버라이드 되었기 때문!
#
#
# # 튼튼한 두팔도 나오게 하려면?
#
# class grandfather:
#     def __init__(self):
#         print("튼튼한 두팔")
#
#
# class father2(grandfather):
#     def __init__(self):
#         super().__init__()
#         print("지혜")
#
#
# arg_father2 = father2()
#
# • super() 의 장점
# ○ super() 를 이용하면 부모 클래스의 멤버에 접근 가능
# ○ super() 를 이용하면 부모 클래스 명이 변경 되어도 일일이 코드를 고치는 수고를 줄일 수 있음.
# ○ super() 를 이용하면 죽음의 다이아몬드 상속 피할 수 있음
#
# • 데코레이터 사용법
# ○ 데코레이터: 함수를 꾸며주는 함수, 함수의 능력을 확장시켜주는 함수
# ○ 어떤 동작 수행 전에 @ 로 시작하는 키워드를 사용해서 수행
# ○ 데코레이터의 중요한 기능
# § 함수를 강력하게 해줌
# § 공통적으로 사용하는 코드를 쉽게 관리하기 위해 사용
#
# ○ 파이썬 함수의 4 가지 특징
# § 변수에 할당 가능
#
#
# def greet(name):
#     return "hello{}".format(name)
#
#
# greet_someone = greet
# print(greet_someone("scott"))
#
# § 다른 함수 내에서 정의될 수 있음
#
# def greeting(name):
#     def greet_message():
#         return 'hello'
#
#     return "{}  {}".format(greet_message(), name)
#
# § 함수의 인자(매개변수) 값으로 전달될 수 있음
#
#
# def greet(name):
#     return "hello {}".format(name)
#
#
# def change_name_greet(func):
#     name = "king"
#     return func(name)
#
#
# print(change_name_greet(greet))
#
# § 함수의 반환값이 될 수 있음
#
#
# def greet(name):  # 이름을 넣어주면 hello 를 앞에 넣어줌
#     return "hello {}".format(name)
#
#
# def uppercase(func):  # 함수의 리턴값을 받아서 대문자로 출력하는 함수
#     def wrapper(name):  # 대문자로 출력하는 기능에 충실한 함수
#         result = func(name)
#         return result.upper()
#
#     return wrapper
#
#
# new_greet = uppercase(greet)
# print(new_greet("scott"))
#
# ○ 데코레이터 표현법을 보기 전에 먼저 데코레이터와 같은 역할을 하는 함수 생성
#
#
# class greet(object):
#     current_user = None  # current_user 라는 변수인 속성을 선언
#
#     def set_name(self, name):  # name 에 admin 이라는 문자가 들어오면
#         if name == 'admin':  # current_user 에 admin 이라는 문자를 담고
#             self.current_user = name
#         else:  # admin 이 아니라면 권한이 없다는 에러 발생
#             raise Exception("권한이 없네요")
#
#     def get_greeting(self, name):  # name 이라는 매개변수에 admin 이 입력되면
#         if name == 'admin':  # hello + name 출력
#             return "hello {}".format(self.current_user)
#
#
# # 클래스 실행방법
#
# class_greet = greet()
# class_greet.set_name('admin')  # admin 대신 딴거를 넣으면 권한 없다고 에러 뜸
# print(class_greet.get_greeting('admin'))
#
#
#
#
#
#
#
#
# • 문제164.책 192 쪽을 보고 초기화하는 코드 추가해서['a'], ['b'] 나오게 하기
#
#
# class ClassVar:
#     def __init__(self):
#         self.text_list = []  # 클래스의 정의 시점에서 바로 메모리에 할당됨
#
#     def add(self, text):
#         self.text_list.append(text)
#
#     def print_list(self):
#         print(self.text_list)
#
#
# if __name__ == '__main__':
#     a = ClassVar()  # 위에서 만든 생성자를 이용해 a라는 실체를 만든다.
#     a.add('a')  # a 라는 객체의 add 기능을 작동
#     a.print_list()  # a 라는 객체의 print_list 기능을 작동
#
#     b = ClassVar()  # 위에서 만든 생성자를 이용해 b라는 객체를 만든다.
#     b.add('b')  # b 객체에 b를 넣는다.
#     b.print_list()  # 출력 결과는 ['a'],   ['a','b'] 가 나옴 why? 초기화하지 않아서 text_list 에 'a' 들어간 상태에서 'b' 가 들어가서 a, b 둘다 나옴
#
#
# • 문제165.머신러닝 코드 입히기 전인 핑퐁 게임을 파이썬으로 구현
# from tkinter import *
# import random
# import time
#
#
# class Ball:
#
#     def __init__(self, canvas, paddle, color):
#             self.canvas = canvas
#
#         self.paddle = paddle
#         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # 공 좌표 및 색깔(oval : object 형태 타입)
#         self.canvas.move(self.id, 245, 100)  # 공을 캔버스 중앙으로 이동
#         starts = [-3, -2, -1, 1, 2, 3]
#         random.shuffle(starts)
#
#          # 공의 속도
#         self.x = starts[0]
#         self.y = -3
#         self.canvas_height = self.canvas.winfo_height()
#         self.canvas_width = self.canvas.winfo_width()
#         self.hit_bottom = False
#
#     def hit_paddle(self, pos):
#             paddle_pos = self.canvas.coords(self.paddle.id)
#
#         if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
#                 if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
#                         return True
#         return False
#
#     def draw(self):
#             self.canvas.move(self.id, self.x, self.y)  # 공을 움직이게 하는 부분
#
#          # 공이 화면 밖으로 나가지 않게 해준다
#         pos = self.canvas.coords(self.id)
#         if pos[1] <= 0:
#                 self.y = 3
#         if pos[3] >= self.canvas_height:  # 바닥에 부딪히면 게임오버
#                 self.hit_bottom = True
#         if pos[0] <= 0:
#                 self.x = 3
#         if pos[2] >= self.canvas_width:
#                 self.x = -3
#         if self.hit_paddle(pos) == True:  # 판에 부딪히면 위로 튕겨올라가게
#                 self.y = -3
#
#
# class Paddle:
#
#     def __init__(self, canvas, color):
#             self.canvas = canvas
#
#         self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
#         self.canvas.move(self.id, 200, 300)
#         self.x = 0
#         self.canvas_width = self.canvas.winfo_width()
#         self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
#         self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
#
#     def draw(self):
#             self.canvas.move(self.id, self.x, 0)
#
#         pos = self.canvas.coords(self.id)
#         if pos[0] <= 0:
#                 self.x = 0
#         elif pos[2] >= self.canvas_width:
#             self.x = 0
#
#     def turn_left(self, evt):
#             self.x = -2
#
#     def turn_right(self, evt):
#             self.x = 2
#
#
# tk = Tk()
# tk.title("Game")
# tk.resizable(0, 0)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()
# paddle = Paddle(canvas, 'blue')
# ball = Ball(canvas, paddle, 'red')
# start = False
# # 공을 약간 움직이고 새로운 위치로 화면을 다시 그리며, 잠깐 잠들었다가 다시 시작해라!
# while 1:
#         if ball.hit_bottom == False:
#                 ball.draw()
#         paddle.draw()
#      # 그림을 다시 그려라! 라고 쉴새없이 명령
#     tk.update_idletasks()
#     tk.update()
#      # 시작 전 2초간 sleep
#     if not start:
#             time.sleep(2)
#         start = True
#     time.sleep(0.01)
#
#
# • 문제166.다이아몬드 상속시 팔이 2 개가 되게 하시오.
#
#
# class grandfather:
#     def __init__(self):
#         print("튼튼한 두팔")
#
#
# class father1(grandfather):
#     def __init__(self):
#         grandfather.__init__(self)
#         print("지식")
#
#
# class father2(grandfather):
#     def __init__(self):
#         grandfather.__init__(self)
#         print("지혜")
#
#
# class grandchild(father1, father2):
#     def __init__(self):
#         father1.__init__(self)
#         father2.__init__(self)
#         print("자기 만족도가 높은 삶")
#
#
# grandchild_object = grandchild()
#
# 튼튼한 두팔
# 지식
# 튼튼한 두팔
# 지혜
# 자기 만족도가 높은 삶  # 다이아몬드 상속 시 grandfather 의 "튼튼한 두팔" 이 두번 나옴
#
#
# # 이걸 해결하려면 ?
#
# class grandfather:
#     def __init__(self):
#         print("튼튼한 두팔")
#
#
# class father1(grandfather):
#     def __init__(self):
#         super().__init__()
#         print("지식")
#
#
# class father2(grandfather):
#     def __init__(self):
#         super().__init__()
#         print("지혜")
#
#
# class grandchild(father1, father2):
#     def __init__(self):
#         super().__init__()
#         print("자기 만족도가 높은 삶")
#
#
# grandchild_object = grandchild()
#
#
# • 문제167.이름 입력하고 함수 실행하면 해당 사원의 직업이 소문자로 출력되는 함수 생성
# 함수1.이름 입력시 직업 출력되는 함수
# 함수2.문자 입력시 소문자로 출력하는 함수
#
# new_find_job = lowercase(find_job)
# print(new_find_job('SCOTT'))
#
#
# def find_job(name):
#     import csv
#     for emp_list in csv.reader(open("C:\data\emp2.csv", 'r')):
#         if emp_list[1] == name:
#             return emp_list[2]
#
#
# def lower_case(func):
#     def wrapper(name):
#         result = func(name).lower()
#         return result
#
#     return wrapper
#
#
# new_find_job = lower_case(find_job)
# print(new_find_job('SCOTT'))
#
# print(lower_case(find_job('SCOTT')))  # 왜인지는 정확히 모르나 이건 안 됨. 중첩함수일 때 안에다가 변수까지 못 써주는듯...?
#
# • 문제168.위 코드에서 중복적으로 사용되는 코드를 떼어내서 함수로 생성(중복되는 코드: admin 이 맞는지 확인하는 코드)
# def is_admin(user_name):
#     if user_name != 'admin':
#         raise Exception('권한이 없다구요!')
#
#
# class greet(object):
#     current_user = None
#
#     def set_name(self, name):
#         is_admin(name)
#         self.current_user = name
#
#     def get_greeting(self, name):
#         is_admin(name)
#         return "hello {}".format(self.current_user)
#
#
# # 클래스 실행방법
#
# class_greet = greet()
# class_greet.set_name('admin')
# print(class_greet.get_greeting('admin'))
# • 문제169.이름 넣어서 함수 실행하면 해당 사원의 월급이 출력되게 하는 함수 생성.KING만 월급을 볼 수 있게 하고, KING이 아니면 권한이 없다고 에러 뜨게
#
#
# def is_king(name, password):
#     if name != 'KING' or password.upper() != 'TIGER':
#         raise Exception('권한이 없습니다.')
#
#
# class find_sal(object):
#     user = None
#
#     def set_name(self, name, password):
#         is_king(name, password)
#         self.user = name
#
#     def get_sal(self, name, password):
#         import csv
#         for emp_list in csv.reader(open('C:\data\emp2.csv', 'r')):
#             if emp_list[1] == name:
#                 sal = emp_list[5]
#         is_king(name, password)
#         return sal
#
#
# find_sal = find_sal()
# find_sal.set_name('KING', 'tiger')
# print(find_sal.get_sal('KING', 'tiger'))
#
# ○  자기 부하직원 월급까지만 볼 수 있게 출력.비밀번호는 사원번호로
#
#
#
#
#
#
#
#
#
# • 문제170.is_admin(name) 이라는 함수를 사용해서 코드 더 좋아짐.이걸 데코레이터 써서 구현해보기
#
#
# def is_admin(func):
#     def wrapper(*arg, **kwargs):  # *arg 는 리스트의 가변 매개변수
#         # **kwargs 는 딕셔너리 가변 매개변수
#         if kwargs.get('name') != 'admin':
#             raise Exception('권한이 없다구요!')
#         return func(*arg, **kwargs)
#
#     return wrapper
#
#
# class greet(object):
#     current_user = None
#
#     @is_admin
#     def set_name(self, name):
#         self.current_user = name
#
#     @is_admin
#     def get_greeting(self, name):
#         return "hello {}".format(self.current_user)
#
#
# # 클래스 실행방법
#
# class_greet = greet()
# class_greet.set_name(name='admin')
# print(class_greet.get_greeting(name='admin'))
#
# • 문제171.문제169의 코드를 데코레이터 함수 이용해서 구현
#
#
# def is_king(func):
#     def wrapper(*arg, **kwargs):
#         if kwargs.get('name') != 'KING' or kwargs.get('password').upper() != 'TIGER':
#             raise Exception('권한이 없습니다.')
#         return func(*arg, **kwargs)
#
#     return wrapper
#
#
# class find_sal(object):
#     user = None
#
#     @is_king
#     def set_name(self, name, password):
#         self.user = name
#
#     @is_king
#     def get_sal(self, name, password):
#         import csv
#         for emp_list in csv.reader(open('C:\data\emp2.csv', 'r')):
#             if emp_list[1] == name:
#                 sal = emp_list[5]
#         return sal
#
#
# find_sal = find_sal()
# find_sal.set_name(name='KING', password='tiger')
# print(find_sal.get_sal(name='KING', password='tiger'))
#
# --------------------------------------------------------------------------------------------------------------------
#
#
# def is_king(func):
#     def wrapper(*arg, **kwargs):
#         if kwargs.get('name') != 'KING' or kwargs.get('password').upper() != 'TIGER':
#             raise Exception('권한이 없습니다.')
#         return func(*arg, **kwargs)
#
#     return wrapper
#
#
# class find_sal(object):
#     user = None
#
#     @is_king
#     def set_name(self, name, password):
#         self.user = name
#
#     # @is_king
#     def get_sal(self, name):
#         import csv
#         for emp_list in csv.reader(open('C:\data\emp2.csv', 'r')):
#             if emp_list[1] == name:
#                 sal = emp_list[1] + '  ' + emp_list[5]
#         return sal
#
#
# find_sal = find_sal()
# find_sal.set_name(name='KING', password='tiger')
# print(find_sal.get_sal(name='SCOTT'))
# ------------------------------------------------------------------------------------------------------------------------
#
#
# def is_king(func):
#     def wrapper(*arg, **kwargs):
#         if kwargs.get('name') != 'KING' or kwargs.get('password').upper() != 'TIGER':
#             raise Exception('권한이 없습니다.')
#         return func(*arg, **kwargs)
#
#     return wrapper
#
#
# class find_sal(object):
#     user = None
#
#     @is_king
#     def set_name(self, name, password):
#         self.user = name
#
#     # @is_king
#     def get_sal(self, name):
#         import pandas as pd
#         emp = pd.read_csv('c:\data\emp.csv')
#         emp_result = emp[['ename', 'sal']][emp['ename'] == name]
#         return emp_result
#
#
# find_sal = find_sal()
# find_sal.set_name(name='KING', password='tiger')
# print(find_sal.get_sal(name='KING'))
#
#
# mit ttt 코드를 이해하기 위한 머신러닝의 종류
1. 지도학습 :
2. 비 지도학습
3. 강화학습

