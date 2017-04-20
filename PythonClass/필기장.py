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
#       emp.groupby('job')['sal'].max()              - 직업별 최대값 출력
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