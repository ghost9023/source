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
# 문제132 함수를 생성하는데 아래와 같이 숫자를 넣어서 실행하면 해당 숫자만큼 숫자가 세로로 출력!
#
# print(break_fun(10))  # 10이 loop문을 중단시킬 숫자
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#
#
# def break_fun(var):
#     num = 1
#     while 1:
#         print(num)
#         if num == var:
#             break
#         num += 1
#
#
# print(break_fun(10))
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#
# 문제133 위의 함수를 수정해서 결과가 가로로 출력!
#
# print(break_fun(10))  # 10이 loop 문을 중단시킬 숫자
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#
#
# def break_fun(var):
#     list = ''
#     num = 1
#     while (True):
#         list = list + str(num) + '  '
#         if num == var:
#             break
#         num += 1
#     print(list)
#
#
# print(break_fun(10))
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#
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
# 문제134 아래와 같이 딕셔너리 형태의 데이터를 만들고 출력!
#
# emp_dic = {'mgr': '7788', 'sal': '1100', 'deptno': '20', 'comm': '0',
#            'job': 'CLERK', 'hiredate': '1983-01-15', 'empno': '7876',
#            'ename': 'ADAMS'}
#
# print(type(emp_dic))
# print(emp_dic)
# print(emp_dic['mgr'])
#
# < class 'dict'>
#
#
# {'mgr': '7788', 'sal': '1100', 'deptno': '20', 'comm': '0', 'job': 'CLERK', 'hiredate': '1983-01-15', 'empno': '7876',
#  'ename': 'ADAMS'}
# 7788
#
# 문제135 6 장에서 배운 for loop 를 이용해서 emp2.csv를 읽어와서 emp_dic 라는 딕셔너리 데이터 유형 만들기!
#
# import csv
#
# emp = []
# emp_file = open("d:\data\emp2.csv", "r")
# emp_csv = csv.reader(emp_file)
#
# for i in emp_csv:
#     emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                 'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
# print(emp)
#
# 문제136 emp 딕셔너리 변수에서 이름만 출력!
#
# import csv
#
# emp = []
# emp_file = open("d:\data\emp2.csv", "r")
# emp_csv = csv.reader(emp_file)
#
# for i in emp_csv:
#     emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                 'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
# for emp_dic in emp:
#     print(emp_dic['ename'])
#
# KING
# BLAKE
# CLARK
# JONES
# MARTIN
# ALLEN
# TURNER
# JAMES
# WARD
# FORD
# SMITH
# SCOTT
# ADAMS
# MILLER
#
# 문제137 이름과 월급과 직업 출력!
#
# import csv
#
# emp = []
# emp_file = open("d:\data\emp2.csv", "r")
# emp_csv = csv.reader(emp_file)
#
# for i in emp_csv:
#     emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                 'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
# for emp_dic in emp:
#     print(emp_dic['ename'], emp_dic['sal'], emp_dic['job'])
#
# KING
# 5000
# PRESIDENT
# BLAKE
# 2850
# MANAGER
# CLARK
# 2450
# MANAGER
# JONES
# 2975
# MANAGER
# MARTIN
# 1250
# SALESMAN
# ALLEN
# 1600
# SALESMAN
# TURNER
# 1500
# SALESMAN
# JAMES
# 950
# CLERK
# WARD
# 1250
# SALESMAN
# FORD
# 3000
# ANALYST
# SMITH
# 800
# CLERK
# SCOTT
# 3000
# ANALYST
# ADAMS
# 1100
# CLERK
# MILLER
# 1300
# CLERK
#
# 문제138(점심시간 문제) dept.csv을 읽어서 딕셔너리 데이터 구조로 저장하고 아래와 같이 수행하면 deptno, dname, loc가 출력!
#
# import csv
#
# dept = []
# dept_file = open("d:\data\dept.csv")
# dept_csv = csv.reader(dept_file)
#
# for i in dept_csv:
#     dept.append({'deptno': i[1], 'dname': i[2], 'loc': i[3]})
#
# for dept_dic in dept:
#     print(dept_dic['deptno'], dept_dic['dname'], dept_dic['loc'])
#
# deptno
# dname
# loc
# 10
# ACCOUNTING
# NEW
# YORK
# 20
# RESEARCH
# DALLAS
# 30
# SALES
# CHICAGO
# 40
# OPERATIONS
# BOSTON
#
# 문제139
# emp.csv
# 와
# dept.csv를
# 각각
# 읽어서
# emp_dic, dept, dic
# 딕셔너리
# 자료형으로
# 만드는
# 스크립트를
# 하나로
# 합치시오
#
# import csv
#
# emp = []
# dept = []
# emp_file = open("d:\data\emp2.csv")
# dept_file = open("d:\data\dept.csv")
# emp_csv = csv.reader(emp_file)
# dept_csv = csv.reader(dept_file)
#
# for i in emp_csv:
#     emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                 'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
# for j in dept_csv:
#     dept.append({'deptno': j[1], 'dname': j[2], 'loc': j[3]})
#
# 문제140 emp와 dept 라는 딕셔너리 자료구조를 만드는 스크립트와 중첩 for loop 문을 이용해서 emp와 dept를 조인시켜서 ename 과 loc출력! (Nested loop조인 방법)
#
#     import csv
#
#     emp = []
#     dept = []
#     emp_file = open("d:\data\emp2.csv")
#     dept_file = open("d:\data\dept.csv")
#     emp_csv = csv.reader(emp_file)
#     dept_csv = csv.reader(dept_file)
#
#     for i in emp_csv:
#         emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                     'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
#     for j in dept_csv:
#         dept.append({'deptno': j[1], 'dname': j[2], 'loc': j[3]})
#
#     for e in emp:
#         for d in dept:
#             if e['deptno'] == d['deptno']:
#                 print(e['ename'], d['loc'])
#
#     KING
#     NEW
#     YORK
#     BLAKE
#     CHICAGO
#     CLARK
#     NEW
#     YORK
#     JONES
#     DALLAS
#     MARTIN
#     CHICAGO
#     ALLEN
#     CHICAGO
#     TURNER
#     CHICAGO
#     JAMES
#     CHICAGO
#     WARD
#     CHICAGO
#     FORD
#     DALLAS
#     SMITH
#     DALLAS
#     SCOTT
#     DALLAS
#     ADAMS
#     DALLAS
#     MILLER
#     NEW
#     YORK
#
#     문제141 부서위치가 DALLAS인 사원들의 이름과 부서위치 출력!
#
#     import csv
#
#     emp = []
#     dept = []
#     emp_file = open("d:\data\emp2.csv")
#     dept_file = open("d:\data\dept.csv")
#     emp_csv = csv.reader(emp_file)
#     dept_csv = csv.reader(dept_file)
#
#     for i in emp_csv:
#         emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                     'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
#     for j in dept_csv:
#         dept.append({'deptno': j[1], 'dname': j[2], 'loc': j[3]})
#
#     for e in emp:
#         for d in dept:
#             if (e['deptno'] == d['deptno']) & (d['loc'] == 'DALLAS'):
#             print(e['ename'], d['loc'])
#
#     JONES
#     DALLAS
#     FORD
#     DALLAS
#     SMITH
#     DALLAS
#     SCOTT
#     DALLAS
#     ADAMS
#     DALLAS
#
#     문제142 위의 스크립트를 이용해서 조인함수 생성!
#
#     print(join(emp, 'ename', dept,, 'loc', deptno))
#
#     import csv
#
#     emp = []
#     dept = []
#     emp_file = open("d:\data\emp2.csv")
#     dept_file = open("d:\data\dept.csv")
#     emp_csv = csv.reader(emp_file)
#     dept_csv = csv.reader(dept_file)
#
#     for i in emp_csv:
#         emp.append({'empno': i[0], 'ename': i[1], 'job': i[2], 'mgr': i[3],
#                     'hiredate': i[4], 'sal': i[5], 'comm': i[6], 'deptno': i[7]})
#
#     for j in dept_csv:
#         dept.append({'deptno': j[1], 'dname': j[2], 'loc': j[3]})
#
#     for e in emp:
#         for d in dept:
#             if (e['deptno'] == d['deptno']) & (d['loc'] == 'DALLAS'):
#                 print(e['ename'], d['loc'])
#
#
#     def join(table1, col1, table2, col2, conn_col):
#         for i in table1:
#             for j in table2:
#                 if i[conn_col] == j[conn_col]:
#                     print(i[col1], j[col2])
#
#
#     print(join(emp, 'ename', dept, 'loc', 'deptno'))
#
#     JONES
#     DALLAS
#     FORD
#     DALLAS
#     SMITH
#     DALLAS
#     SCOTT
#     DALLAS
#     ADAMS
#     DALLAS
#     KING
#     NEW
#     YORK
#     BLAKE
#     CHICAGO
#     CLARK
#     NEW
#     YORK
#     JONES
#     DALLAS
#     MARTIN
#     CHICAGO
#     ALLEN
#     CHICAGO
#     TURNER
#     CHICAGO
#     JAMES
#     CHICAGO
#     WARD
#     CHICAGO
#     FORD
#     DALLAS
#     SMITH
#     DALLAS
#     SCOTT
#     DALLAS
#     ADAMS
#     DALLAS
#     MILLER
#     NEW
#     YORK
#
#     문제143
#     pandas를
#     이용해서
#     ename, loc
#     출력!
#
#     import pandas as pd
#
#     emp = pd.read_csv("d:\data\emp.csv")
#     dept = pd.read_csv("d:\data\dept.csv")
#
#     result = pd.merge(emp, dept, on='deptno')
#
#     print(result[['ename', 'loc']])
#
#     ename
#     loc
#     0
#     KING
#     NEW
#     YORK
#     1
#     CLARK
#     NEW
#     YORK
#     2
#     MILLER
#     NEW
#     YORK
#     3
#     BLAKE
#     CHICAGO
#     4
#     MARTIN
#     CHICAGO
#     5
#     ALLEN
#     CHICAGO
#     6
#     TURNER
#     CHICAGO
#     7
#     JAMES
#     CHICAGO
#     8
#     WARD
#     CHICAGO
#     9
#     JONES
#     DALLAS
#     10
#     FORD
#     DALLAS
#     11
#     SMITH
#     DALLAS
#     12
#     SCOTT
#     DALLAS
#     13
#     ADAMS
#     DALLAS
#
#     문제144
#     부서위치가
#     DALLAS인
#     사원들의
#     이름과
#     부서위치
#     출력!
#
#     import pandas as pd
#
#     emp = pd.read_csv("d:\data\emp.csv")
#     dept = pd.read_csv("d:\data\dept.csv")
#
#     res = pd.merge(emp, dept, on='deptno')
#     result = res[['ename', 'loc']][res['loc'] == 'DALLAS']
#
#     print(result)
#
#     ename
#     loc
#     9
#     JONES
#     DALLAS
#     10
#     FORD
#     DALLAS
#     11
#     SMITH
#     DALLAS
#     12
#     SCOTT
#     DALLAS
#     13
#     ADAMS
#     DALLAS
#
#     문제145 이름과 부서위치를 출력하는데 아래와 같이 Outerjoin 구현!
#
#     select
#     e.ename, d.loc
#     from emp e, dept
#
#     d
#     where
#     e.deptno = d.deptno(+);
#
#     import pandas as pd
#
#     emp = pd.read_csv("d:\data\emp.csv")
#     dept = pd.read_csv("d:\data\dept.csv")
#
#     res = pd.merge(emp, dept, on='deptno', how='right')
#     result = res[['ename', 'loc']]
#
#     print(result)
#
#     ename
#     loc
#     0
#     KING
#     NEW
#     YORK
#     1
#     CLARK
#     NEW
#     YORK
#     2
#     MILLER
#     NEW
#     YORK
#     3
#     BLAKE
#     CHICAGO
#     4
#     MARTIN
#     CHICAGO
#     5
#     ALLEN
#     CHICAGO
#     6
#     TURNER
#     CHICAGO
#     7
#     JAMES
#     CHICAGO
#     8
#     WARD
#     CHICAGO
#     9
#     JONES
#     DALLAS
#     10
#     FORD
#     DALLAS
#     11
#     SMITH
#     DALLAS
#     12
#     SCOTT
#     DALLAS
#     13
#     ADAMS
#     DALLAS
#     14
#     NaN
#     BOSTON
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
# 5
#
# 문제146 아래와 같이 이름을 입력해서 함수를 실행하면 해당 사원의 부서위치가 출력!
#
# print(find_loc('SMITH'))
#
# DALLAS
#
# import pandas as pd
#
#
# def find_loc(ename):
#     emp = pd.read_csv("d:\data\emp.csv")
#     dept = pd.read_csv("d:\data\dept.csv")
#
#     res = pd.merge(emp, dept, on='deptno')
#     result = res[['loc']][res['ename'] == ename]
#
#     return result
#
#
# print(find_loc('SMITH'))
#
# loc
# 11
# DALLAS
#
# 문제147 미분계수를 구하는 함수를 생성하는데 함수 f(x) = 2 X ^ 2 + 1 일때 x가 - 2 일때 기울기(미분계수) 를 구하시오!
#
# print(mibon_fun(-2))
#
# x가 - 2 에서의 기울기는 - 8 입니다
#
#
# def minbon_fun(num):
#
#
# delta = 0.0001
# result = ((2 * (num + delta) * (num + delta) + 1) - (2 * num * num + 1)) / delta
# return result
#
# print(minbon_fun(-2))
#
#
# def minbon_fun(num):
#     delta = 0.0001
#     result = ((2 * pow((num + delta), 2) + 1) - (2 * pow(num, 2) + 1)) / delta
#     return result
#
#
# print(minbon_fun(-2))
#
# -7.999800000000334
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
# 문제148 함수 f(x) = x ^ 2 - x + 5 에서 x가 - 2 일때의 미분계수!
#
# def numerical_diff(f, x):
#     delta = 0.0001  # 1e-4 로 해도 된다
#     return (f(x + delta) - f(x - delta)) / (2 * delta)
#
#
# def function_1(x):
#     return pow(x, 2) - x + 5
#
#
# print(numerical_diff(function_1, -2))
#
# -5.000000000006111
