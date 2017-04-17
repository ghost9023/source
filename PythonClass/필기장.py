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
#         ○ 기타 연산자
#             between and   ->   <= & >=
#             in            ->   in
#             is null       ->   == ''
#             like          ->   ^, $, 정규식 함수
#             ||            ->   +
#
