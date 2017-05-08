# • 문제1. 위의 리스트 변수에서 1000을 출력
# c = [1000, 2000, 3000, 4000]
# print(c[0])
#
# • 문제2. 리스트 변수 안에 있는 요소들을 하나씩 출력
# c = [1000, 2000, 3000, 4000]
# for i in c:
#     print(i)  # print 앞에 띄어쓰기 해야함!!!!
#
# for i in range(100):
#     print(i + 1)  # range(100) 0~100까지 숫자
#
# • 문제3. a라는 리스트 변수에 아래의 내용을 담으시오
# a = ['7839', 'KING', 'PRESIDENT', '0', '1981-11-17', '5000', '', '10']
#
# • 문제4. a라는 변수 안에 있는 요소들을 끄집어내서 출력
# for i in a:
#     print(i)
#
# • 문제5. a리스트 변수에서 7839만 출력
# print(a[0])
#
# print(type(a[0])): a = ['7839'...라고 했으므로 7839를 글자로 인식
#
# • 문제6. 카페에서 파이썬 수업자료의 emp2.csv 내려받아 c드라이브 밑에 data 폴더에 다운받기
#
# import csv  # csv라는 모듈을  쓰겠다
#
# file = open("C:\data\emp2.csv", 'r')  # c의 emp2.csv를 열어서 file 이라는 변수에 넣겠다.
# emp_csv = csv.reader(file)  # file을 csv.reader로 읽어서 emp_csv 라는 변수에 넣겠다.
# for emp_list in emp_csv:
#     print(emp_list)
#
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):  # 이것도 됨
#     print(emp_list1)
#
# • 문제7. 사원번호만 출력 file = open("C:\data\emp2.csv", 'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#     print(emp_list[0])
#
# • 문제8. 이름과 월급 출력
# file = open("C:\data\emp2.csv", 'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#     print(emp_list[1], emp_list[5])
#
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):
#     print(emp_list1[1], emp_list1[5])
#
# • 문제9. 14개의 리스트 변수 요소 개수를 출력
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):
#     print(len(emp_list1))
#
# • 문제10. 이름과 이름의 길이를 아래와 같이 출력
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):
#     print(emp_list1[1], len(emp_list1[1]))
#
# • 문제11. 사원번호, 이름, 월급 출력
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):
#     print(emp_list1[0], emp_list1[1], emp_list1[5])
#
# • 문제12. 이름, 연봉 출력
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):
#     print(emp_list1[1], emp_list1[5] * 12)  # 이게 안 되는 이유 : sal 부분이 문자형식으로 돼있으므로!!
#
# import csv
#
# for emp_list1 in csv.reader(open("C:\data\emp2.csv", 'r')):
#     print(emp_list1[1], int(emp_list1[5]) * 12)  # int : 숫자로 형변환하는 함수
#
# • 문제13. 이름, 커미션 출력.커미션이 none 이면 0 으로 출력
#
# def ifnull(var, val):      # def : 사용자 정의 함수 선언
#     if var is '':
#         return val
#     return var
#
#
# import csv
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1], ifnull(emp_list1[6], 0))
#
# • 문제14. 이름과 월급 + 커미션 출력
#
#
# def nvl(var, val):
#     if var is '':
#         return val
#     return var
#
#
# import csv
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1], int(emp_list1[5]) + int(nvl(emp_list1[6], 0)))
#
# ○ 다른 문제: 두 수의 최대공약수
#
# def gong(a, b):
#     if a >= b:
#         for i in range(b):
#             if a % (b - i) + b % (b - i) is 0:
#                 return '최대공약수는', b - i, '입니다.'
#     for j in range(a):
#         if a % (a - j) + b % (a - j) is 0:
#             return '최대공약수는', a - j, '입니다.'
#
# ○ 다른 문제: 홀수 짝수
#
#
# def holjjack(a):
#     if a % 2 is 1:
#         return '홀수'
#     return '짝수'
#
# ○ 다른 문제: 버블정렬
#
#
# def bubble(a):
#     for k in range(len(a) - 1):
#         for i in range(len(a) - 1):
#             if a[i] >= a[i + 1]:
#                 j = a[i]
#                 a[i] = a[i + 1]
#                 a[i + 1] = j
#     for m in range(len(a)):
#         print(a[m])
#
#
# a = [1, 4, 6, 2, 7, 89, 3]
# print(bubble(a))
#
# ○ 다른 문제: 여러 수의 최대공약수 풀기
#
# def manygong(a):
#     sum = 0
#     for i in range(len(a) - 1):
#         for j in range(len(a) - 1):
#             if a[j] >= a[j + 1]:
#                 J = a[j]
#                 a[j] = a[j + 1]
#                 a[j + 1] = J
#
#     for k in range(a[0]):
#         sum = 0
#         for l in range(len(a)):
#             sum = sum + a[l] % (a[0] - k)
#             result = (a[0] - k)
#         if sum is 0:
#             return result
#
# • 문제15. 이름과 직업 출력 소문자로
# import csv
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1].lower(), emp_list1[2].lower())
# • 문제16. 이름 출력.이름의 첫번째 철자만 뽑아서 소문자로 출력
# import csv
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1][0:1].lower())
#
# • 문제17. 이름 출력하는데 이름의 두번째 철자부터 마지막까지 소문자로 출력
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1][1:len(emp_list1) - 1].lower())
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1][1:].lower())
#
# • 문제18. initcap 사용자 함수 만들기 이름 첫번째 철자는 대문자 출력 나머지는 소문자 출력
# initcap(emp_list[1])
#
#
# def initcap(a):
#     return a[:1].upper() + a[1:].lower()
#
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(initcap(emp_list1[1]))
#
# • 문제19. 이름의 첫번째 철자부터 세번째 철자까지 출력할 수 있는 substr 함수 만들기
#
# def substr(a, b, c):
#     return a[b - 1:b - 1 + c]
#
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(substr(emp_list1[1], 2, 3))
#
# a[a:b]  -> a번째수부터(b - 1) 번째 수까지 나오게 단, 맨 첫글자는 0 번째 수라고 했을때
#
# • 문제21. 이름과 월급 출력하는데 월급 출력할 때 0 대신 * 출력
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1], emp_list1[5].replace('0', '*'))  # 0이 숫자형인지 문자형인지 파악해야함.
#
# • 문제22. 이름과 월급 출력. 0 ~2 는 * 로 출력
# import re  # 정규식 모듈 import
# import csv
#
# for emp_list1 in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list1[1], re.sub('[0-2]', '*', emp_list1[5]))  # re.sub(a, b, c) : regexp_substr(c,a,b)
#
# http: // devanix.tistory.com / 296  # 정규식 참고 사이트
#
# • 문제23. 이름과 이름의 길이 출력
# for emp_list in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp_list[1], len(emp_list[1]))
#
# • 문제24. 아래와 split 함수의 예제를 수행해보시오! file = 'a b c d e f g'
# print(file.split(' '))  # 공백 ' ' 별로 단어를 쪼개라
#
# • 문제25. file 변수의 요소들을 리스트 변수로 담아내서 두번째 요소인 b 만 출력
# file = 'a b c d e f g'
# print(file.split(' ')[1])
#
# • 문제26. 겨울왕국 대본을 공백 구분으로 두고 나눠서 리스트 변수로 저장
# for winter_list in open("C:\data\winter.txt", 'r'):
#     print(winter_list.split(' '))
#
# • 문제27. 겨울왕국에는 단어가 총 몇개 있는지 출력
# cnt = 0
# sum = 0
# for winter_list in open("C:\data\winter.txt", 'r'):
#     cnt = cnt + 1
#     sum = sum + len(winter_list.split(' '))
#     print('해당 리스트의 단어수는', len(winter_list.split(' ')), '개 입니다.')
# print('합계는', sum, '개 입니다.')
# print('평균 단어수는', round(sum / cnt, 2), '입니다.')
#
# ○ 다른 문제: 평균 글자수, 리스트 내 단어수, 총 합계 단어수, 모든 문장의 평균 단어수, 모든 문장의 평균 글자수 구하기
#
# def count_l(a):
#     sum = 0
#     cnt = 0
#     for i in range(len(a.split(' '))):
#         cnt += 1
#         sum += len(a.split(' ')[i - 1])
#     return round((sum / cnt), 2)
#
#
# cnt = 0
# sum = 0
# sum_l = 0
# for winter_list in open("C:\data\winter.txt", 'r'):
#     cnt += 1
#     sum += len(winter_list.split(' '))
#     sum_l += count_l(winter_list)
#     print(cnt, '행의 평균 글자수는', count_l(winter_list), '입니다.')
#     print('---- 리스트의 단어수는', len(winter_list.split(' ')), '개 입니다.')
# print('합계는', sum, '개 입니다.')
# print('평균 단어수는', round(sum / cnt, 2), '입니다.')
# print('평균 글자수는', round(sum_l / cnt, 2), '입니다.')
#
# • 문제29. 겨울왕국 대본에는 elsa가 몇번 나오는지 카운트
# sum = 0
# for winter_list in open("C:\data\winter.txt", 'r'):
#     cnt = winter_list.split(' ').count('Elsa')
#     sum += cnt
# print(sum)
#
# • 문제30. emp.csv에서 14개의 리스트 변수 중 5 번째 요소(월급)만 담아서 리스트변수 생성
# sal_list = []
# for emp in csv.reader(open("C:\data\emp2.csv", 'r')):
#     sal_list.append(emp[5])
# print(sal_list)
#
# • 문제31. 겨울왕국 대본을 단어별로 출력
# for winter_list in open("C:\data\winter.txt", 'r'):
#     for i in range(len(winter_list.split(' '))):
#         print(winter_list.split(' ')[i])
#
# for winter_list in open("C:\data\winter.txt", 'r'):
#     for i in winter_list.split(' '):  # 리스트 변수 ----> 단어
#         print(i)
# • 문제32. append 함수 이용해서 단어들을 하나의 리스트 변수에 담기
# all_list = []
# for winter_list in open("C:\data\winter.txt", 'r'):
#     for i in winter_list.split(' '):
#         all_list.append(i)
#
# print(all_list)
#
# • 문제33. 겨울왕국을 공백기준해서 자른 다음 리스트로 저장
# win = []
# file = open("d:/data/winter.txt", "r")
# for winter_list in file:
#     a = winter_list.split(' ')
#     for i in a:
#         b = i.strip('\n')
#         print(win.append(b))
# print(win)
#
# • 문제34.
#
#
# • 문제35. instr함수를 파이썬으로 구현
# def instr(word, target):
#     for i in range(len(word)):
#         if word[i] == target:
#             return i+1
# word = 'epikhigh'
# result = instr(word, 'h')
# print (result)
#
# • 문제36. 이름, 이름의 M자가 몇번째 자리에 있는지 출력
# def instr(word, target):
#     for i in range(len(word)):
#         if word[i] == target:
#             return i+1
#
# import csv
# file = open("d:\data\emp_comm.csv", 'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#     print(emp_list[1], instr(emp_list[1], 'M'))
#
# • 문제37. 이름, 월급, 보너스(월급의 15%)를 출력
# import csv
# file = open("d:\data\emp_comm.csv", 'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#     print(emp_list[1], emp_list[5], int(emp_list[5])*0.15)
#
# • 문제38. 위의 결과를 컬럼명도 출력되게
# import csv
# file = open("d:\data\emp_comm.csv", 'r')
# emp_csv = csv.reader(file)
# print('이름', '월급', '보너스')
# for emp_list in emp_csv:
#     print(emp_list[1], emp_list[5], int(emp_list[5])*0.15)
#
# • 문제39. 위의 결과를 반올림
# import csv
# file = open("d:\data\emp_comm.csv", 'r')
# emp_csv = csv.reader(file)
# print('이름', '월급', '보너스')
# for emp_list in emp_csv:
#     print(emp_list[1], emp_list[5], round(int(emp_list[5])*0.15))
#
# • 문제40. 보너스를 출력할 때 소숫점 이하를 trunc를 써서 잘라내서 출력
# import csv
# file = open("d:\data\emp_comm.csv", 'r')
# emp_csv = csv.reader(file)
# print('이름', '월급', '보너스')
# import math
# for emp_list in emp_csv:
#     print(emp_list[1], emp_list[5], math.trunc(int(emp_list[5])*0.15))
#
# • 문제41. input 명령어를 이용해서 숫자를 입력받고 해당 숫자가 짝수인지 홀수인지 출력
# a = int(input('첫번째 숫자를 입력'))
#
# def odd_even(a):
#     if a % 2 == 1:
#         return '홀수'
#      return '짝수'
#  print (odd_even(a))
#
#  • 문제42. power 함수를 이용해서 숫자를 입력 받아 지수를 계산
#  a = int(input('밑수를 입력'))
#  b = int(input('지수를 입력'))
#  import math
#  math.pow(a, b)
#
#  • 문제43. 오늘부터 3달 뒤의 날짜를 출력
# from datetime import date
# from dateutil.relativedelta import relativedelta
# edt = date.today() + relativedelta(months=+3)
# print(date.today(), edt)
#
#  • 문제44. 이름, 입사일, 입사일로부터 3달 후의 날짜 출력
# import csv
# import datetime
# from dateutil.relativedelta import relativedelta
# file = open("D:\data\emp2.csv", 'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#      a = datetime.datetime.strptime(emp_list[4], '%Y-%m-%d')
#      print(emp_list[1], emp_list[4], a + relativedelta(months=+3))
#
#  • 문제46. 올해 2월달의 마지막 날짜를 출력
#
#
#
#  • 문제47. 오늘부터 이번달 말일 까지 몇일 남았는가 출력
# from datetime import date
# from calendar import monthrange
# print(monthrange(2017,4)[1])
# print(date.today().day)
# print(monthrange(2017,4)[1] - date.today().day )
#
#  • 문제48. 오늘이 무슨 요일인지 출력
# from datetime import date
# print(date.today())
# print(date.today().weekday())
#
# days=['월','화','수','목','금','토','일']
#
# print(days[date.today().weekday()])
#
#  • 문제49. 이름, 입사일을 출력
# import csv
# import datetime
# file = open("D:\data\emp2.csv", 'r')
# emp_csv = csv.reader(file)
# days=['월','화','수','목','금','토','일']
# print('이름', '입사일', '입사 요일')
# for emp_list in emp_csv:
#      a = datetime.datetime.strptime(emp_list[4], '%Y-%m-%d')
#      print(emp_list[1], emp_list[4], days[a.weekday()])
#
#  • 문제50.
# from datetime import date
# import datetime
# print(date.today()+datetime.timedelta(days=1) )
#
#  • 문제51. 아래와 같이 실행되는 사용자 정의 함수를 생성
# from datetime import date
# import datetime
# def next_day(date, a):
#     a=int(a)
#     return (date+datetime.timedelta(days=a))
#
# print(next_day(date.today(),1))
#
#  • 문제52. 문자형을 입력받아 아래와 같이 실행되는 사용자 정의 함수를 생성
# from datetime import date
# import datetime
# def next_day(date, a):
#     date=datetime.datetime.strptime(date,'%Y-%m-%d')  - 문자형을 날짜형으로 형변환
#     a=int(a)
#     return (date+datetime.timedelta(days=a))
#
# print(next_day('2017-04-17',1))
#
#  • 문제53. 지정된 날짜에서 돌아오는 요일의 날짜가 출력되게 실행
# import datetime
# from datetime import date
# def next_day(dt, ds):
#     dic={}
#     dic['월요일'] =0
#     dic['화요일'] =1
#     dic['수요일'] =2
#     dic['목요일'] =3
#     dic['금요일'] =4
#     dic['토요일'] =5
#     dic['일요일'] =6
#     c=dic[ds]
#     d=date.today().weekday()
#     dt = datetime.datetime.strptime(dt, '%Y-%m-%d')
#     if c-d == 0 : c=7
#     elif c-d != 0 : c=dic[ds]
#     return (dt+datetime.timedelta(days=c))
# print(next_day('2017-04-17','월요일'))
#
# • 문제54.이름, 입사한 날짜부터 오늘까지 총 며칠 근무했는지 출력
# import datetime
# import csv
#
# for emp in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     print(emp[1],
#           (date.today() - datetime.datetime.strptime(emp[4], '%Y-%m-%d').date()))  # .date() 날짜형으로 출력   날짜형을 바꿔줘야함.
#
# date.today() --> datetime.date형식
# datetime.datetime.strptime(emp[4], '%Y-%m-%d')    -> datetime.datetime형식
# datetime.datetime.strptime(emp[4], '%Y-%m-%d').date() --> datetime.date형식
#
# • 문제55. if 문 활용하여 사원번호가 7788 인 사원의 사원이름과 월급 출력
# import csv
#
# for emp in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     if int(emp[0]) == 7788:
#         print(emp[1] and emp[5])
#
# • 문제56. 월급 3000이상인 사원들의 이름과 월급 출력
# import csv
#
# for emp in csv.reader(open("C:\data\emp_comm.csv", 'r')):
#     if int(emp[5]) >= 3000:
#         print(emp[1], emp[5])
#
# • 문제57. 1981년 11월 17일에 입사한 사원의 이름, 입사일 출력
# import csv
# for emp_list in csv.reader(open("D:\data\emp_comm.csv", 'r')):
#     if emp_list[4] == '1981-11-17':
#         print(emp_list[1], emp_list[4])
#
# • 문제58. 81년도에 입사한 사원들의 이름, 입사일 출력(날짜형 변환 없이)
#import csv
# for emp_list in csv.reader(open("D:\data\emp_comm.csv", 'r')):
#     if emp_list[4].split('-')[0] == '1981':
#         print(emp_list[1], emp_list[4].split('-')[0], emp_list[4].split('-')[0][2:4])
#
# • 문제59. 아래의 리스트 변수에서 positive 단어는 몇개 나오는가?
# word=['winter','cold','positive','negative','positive','positive','positive','positive','positive']
# sum=0
# for i in word:
#     if 'positive'== i:
#         sum=sum+1
# print(sum)
#
# • 문제60. 아래의 리스트 변수에서 positive, negative 단어는 몇개 나오는가?
# word=['winter','cold','positive','negative','positive','positive','negative']
# sum=0
# for i in word:
#     if i in ['positive','negative']:
#         sum=sum+1
# print(sum)
#
# • 문제61. 겨울왕국엔 긍정단어가 몇개나 들어았는가?
# wint=[]
# positive = []
# file = open("D:\data\winter.txt", 'r')
# for winter_list in file:
#     low = winter_list.lower()
#     win_split = low.split(' ')
#     for i in win_split:
#         i = i.strip()
#         wint.append(i)
# sum = 0
# for i in wint:
#     for word in positive:
#         if word in i:
#             sum += 1
#
# print(sum)
#
# • 문제62. 직업이 SALESMAN이고 월급이 1200이상인 사원들의 이름과 직업과 월급을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', '  직업  ', '월급')
# for emp_list in emp_csv:
#         if (emp_list[2]=='SALESMAN') & (int(emp_list[5]) >= 1200):
#             print(emp_list[1], emp_list[2], emp_list[5])
#
# • 문제63. 월급이 1000에서 3000 사이인 사원들의 이름과 월급을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', '월급')
# for emp_list in emp_csv:
#         if 1000 <= int(emp_list[5]) <= 3000:
#             print(emp_list[1], emp_list[2], emp_list[5])
#
# • 문제64. 직업이 ANALYST, CLERK인 사원들의 이름과 월급과 직업을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', ' 직업 ' '월급')
# for emp_list in emp_csv:
#         if emp_list[2] in ['ANALYST', 'CLERK']:
#             print(emp_list[1], emp_list[2], emp_list[5])
#
# • 문제65. 직업이 ANALYST, CLERK가 아닌 사원들의 이름과 월급과 직업을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', ' 직업 ' '월급')
# for emp_list in emp_csv:
#         if emp_list[2] not in ['ANALYST', 'CLERK']:
#             print(emp_list[1], emp_list[2], emp_list[5])
#
# • 문제66. 커미션이 null인 사원들의 이름과 커미션을 출력
# import csv
# file = open("D:/data/emp_comm.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', '커미션')
# for emp_list in emp_csv:
#         if emp_list[6] is '':
#             print(emp_list[1], emp_list[6])
#
# • 문제67. 커미션이 null이 아닌 사원들의 이름과 커미션을 출력
# import csv
# file = open("D:/data/emp_comm.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', '커미션')
# for emp_list in emp_csv:
#         if emp_list[6] != '':
#             print(emp_list[1], emp_list[6])
#
# • 문제68. 이름의 첫 글자가 S로 시작하는 사원들의 이름과 월급을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', ' 월급 ')
# for emp_list in emp_csv:
#         if emp_list[1][0:1] == 'S':
#             print(emp_list[1], emp_list[5])
#
# • 문제69. 이름의 두 번째 글자가 M인 사원들의 이름과 월급을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', ' 월급 ')
# for emp_list in emp_csv:
#         if emp_list[1][1:2] == 'M':
#             print(emp_list[1], emp_list[5])
#
# • 문제70. 이름의 마지막 글자가 H인 사원들의 이름과 월급을 출력
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# print(' 이름', ' 월급 ')
# for emp_list in emp_csv:
#         if emp_list[1][-1] == 'H':
#             print(emp_list[1], emp_list[5])
#
# • 문제71. emp_list 리스트 변수를 선언하고 input 명령어를 이용해서 리스트 변수에 추가할 요소를 입력받아 추가
# emp_list=[]
# a = input('A리스트에 추가할 요소를 입력하세요')
# emp_list.append(a)
# print(A)
#
# • 문제72. 위에서 입력한 변수를 제거
# a = input('A리스트에 제거할 요소를 입력하세요')
# emp_list.remove(a)
# print(A)
#
# • 문제73. 위 코드를 바꿔서 1번을 입력받으면 1번, 삭제는 2번, 갯수확인은 3번이 되게 실행
# emp_list=['1', '2', '3', '4']
# num = input('리스트 요소 추가는 1번, 제거는 2번, 갯수확인은 3번을 입력하세요')
# print(num,'을 입력하셨습니다.')
# if int(num) == 1:
#     num1 = input('A리스트에 추가할 요소를 입력하세요')
#     emp_list.append(num1)
#     print(emp_list)
# elif int(num) == 2:
#     num2 = input('A리스트에서 제거할 요소를 입력하세요')
#     for i in emp_list:
#         if i != num2:
#             print('입력된 자료는 없습니다')
#     emp_list.remove(num2)
#     print(emp_list)
# elif int(num) == 3:
#     print(len(emp_list))
#
# • 문제74. sort를 이용해서 월급을 높은 것 부터 출력(sal_list 라는 비어있는 리스트에 emp_list의 5번쨰 요소를 for loop로 담아 실행)
# import csv
# file = open("D:/data/emp2.csv","r")
# emp_csv = csv.reader(file)
# sal_list=[]
# for emp_list in emp_csv:
#     sal_list.append(int(emp_list[5]))
# sal_list.sort(reverse=True)
# print(sal_list)
# for i in sal_list:
#     print(i)
# -----------------------------------------
# import csv
#
# #sorted 함수에서 비교 대상으로 사용할 대상 리턴
# #int(data[5]) : int로 형변환한 월급
# def salCheck(data):
#     return int(data[5])
#
# file = open("D:\data\emp2.csv", "r")
# emp_csv = csv.reader(file)
# emp_list = []
# for i in emp_csv:
#     emp_list.append(i)
#
# emp_list_sorted = sorted(emp_list, reverse=True, key=salCheck)
#
# for i in emp_list_sorted:
#     print(i[1], i[5])
#
# • 문제75. 이름과 월급을 이름이 ABC순으로 정렬해서 출력
# import csv
#
# def enameCheck(data):
#     return (data[1])
#
# file = open("D:\data\emp2.csv", "r")
# emp_csv = csv.reader(file)
# emp_list = []
# for i in emp_csv:
#     emp_list.append(i)
#
# emp_list_sorted = sorted(emp_list, reverse=False, key=enameCheck)
#
# for i in emp_list_sorted:
#     print(i[1], i[5])
#
# • 문제76. 직업이 SALESMAN인 사원들의 이름, 입사일, 직업을 최근 입사일 기준으로 출력
# import csv
#
# def hiredateCheck(data):
#     return (data[4])
#
# file = open("D:\data\emp2.csv", "r")
# emp_csv = csv.reader(file)
# emp_list = []
# for i in emp_csv:
#     emp_list.append(i)
#
# emp_list_sorted = sorted(emp_list, reverse=True, key=hiredateCheck)
#
# for i in emp_list_sorted:
#     if i[2] == 'SALESMAN':
#         print(i[1], i[2], i[4])
#
# • 문제77. emp_list에서 최대 월급을 출력
# import csv
#
# def salCheck(data):
#     return (data[5])
#
# file = open("D:\data\emp2.csv", "r")
# emp_csv = csv.reader(file)
# sal_list = []
# for emp_list in emp_csv:
#     sal_list.append(int(emp_list[5]))
#
# print(sal_list)
# print(max(sal_list))
#
# • 문제78. emp_list에서 평균 월급을 출력
#
# import csv
#
# def salCheck(data):
#     return (data[5])
#
# file = open("D:\data\emp2.csv", "r")
# emp_csv = csv.reader(file)
# sal_list = []
# for emp_list in emp_csv:
#     sal_list.append(int(emp_list[5]))
#
# print(sal_list)
# print(round(sum(sal_list)/len(sal_list)))
#
# • 문제79. emp_list에서 직업이 SALESMAN인 사원 중 최대 월급을 출력
# import csv
#
# def salCheck(data):
#     return (data[5])
# file = open("D:\data\emp2.csv", "r")
# emp_csv = csv.reader(file)
# sal_list = []
# for emp_list in emp_csv:
#     if emp_list[2] == 'SALESMAN':
#         sal_list.append(int(emp_list[5]))
#
# print('SALESMAN MAX SAL : ',max(sal_list))
#
# • 문제80. (SQL문제) 아래와 같은 상황일때 플레이어1이 둘 때 가장 유리한 수가 무엇인가?
#           (c5, c6, c8 중 어디에 1을 두어야 가장 유리한가?)
#                  1   2   1
#                  2   0   0
#                  1   0   2
#
# select c5, max(val_new) from ttt_data
# where c1=1 and c2=2 and c3=1 and c4=2 and c7=1 and c9=2
# group by c5;
# select c6, max(val_new) from ttt_data
# where c1=1 and c2=2 and c3=1 and c4=2 and c7=1 and c9=2
# group by c6;
# select c8, max(val_new) from ttt_data
# where c1=1 and c2=2 and c3=1 and c4=2 and c7=1 and c9=2
# group by c8;
#
# 해석 : 플레이어1, 플레이어2 모두 가중치가 같은 곳은 서로간 유불리가 없는 곳이라 불 필요한 곳인 것을 의미한다. 따라서
#       위 쿼리로 봤을 때 c6 c8은 가중치가 다 1이어서 버리는 곳이지만 c5는 플1의 가중치가 0.995, 플2의 가중치가 0.005로
#       플1의 입장에선 c5에 두는 것이 가장 우월한 수가 된다.
#
# • 문제81. ttt_data를 불러오기
# 컬럼명 : C1,C2,C3,C4,C5,C6,C7,C8,C9,VAL_OLD,VAL_NEW,PLAYER,GAME_NUM,LEARNING_ORDER
# import csv
#
# file = open("D:/data/ttt_data.csv", "r")
# ttt_csv = csv.reader(file)
#
# print('C1','C2','C3','C4','C5','C6','C7','C8','C9','VAL_OLD','VAL_NEW','PLAYER','GAME_NUM','LEARNING_ORDER')
# for i in ttt_csv:
#     print(i)
#
# • 문제82. pandas 모듈을 이용해서 사원테이블에서 최대 월급을 출력
# import pandas as pd
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# print(emp['sal'].max())
#
# • 문제83. 직업이 SALESMAN인 사원들의 이름과 월급과 직업을 출력
# import pandas as pd
#
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# result = emp[['ename', 'sal']][emp['job'] == 'SALESMAN']
#             #열 조건                #행 조건
# print(result)
#
# • 문제84. 월급이 3천 이상인 사원들의 이름과 월급 출력
# import pandas as pd
#
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# result = emp[['ename', 'sal']][emp['sal'] >= 3000]
#             #열 조건                #행 조건
# print(result)
#
# • 문제85. 위의 결과를 월급이 낮은 사원부터 출력
# import pandas as pd
#
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# result = emp[['ename', 'sal']][emp['sal'] >= 3000].sort_values('sal',ascending=True)
# print(result)
#
# • 문제86. 부서번호가 20번인 사원들의 최대월급을 출력
# import pandas as pd
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# result = emp['sal'][emp['deptno'] == 20].max()
# print(result)
#
# • 문제87. 직업, 직업별 토탈월급 출력
# import pandas as pd
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# result = emp.groupby('job')['sal'].sum()
# print(result)
#
# • 문제88. 부서번호, 부서번호별 평균월급 출력
# import pandas as pd
# emp = pd.DataFrame.from_csv("d:\data\emp.csv")
# result = emp.groupby('deptno')['sal'].mean()
# print(result)
#
# • 문제89. 아래의 결과를 pandas로 구현
# select max(learning_order) from ttt_data where player = 1
# and c1 = 1 and c2 = 2 and c3 = 1 and c4 = 2 and c7 = 1 and c9 = 2 and c5+c6+c8 = 1
# group by c5, c6, c8;
# -------------------------
# import pandas as pd
# t_dt = pd.DataFrame.from_csv("d:\data\mit_t.csv")
# result1 = t_dt[(t_dt['PLAYER']==1) &
#                (t_dt['C1'] == 1) &
#                (t_dt['C2'] == 2) &
#                (t_dt['C3'] == 1) &
#                (t_dt['C4'] == 2) &
#                (t_dt['C7'] == 1) &
#                (t_dt['C9'] == 2) &
#                (t_dt['C5'] + t_dt['C6'] + t_dt['C8'] == 1)]
# result2 = result1.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max()
# print(result2)
#
# • 문제90. 직업이 SALESMAN인 사원들의 이름과 월급과 직업을 출력
# -Pandas를 쓰지 않고
# import csv
# file=open("D:/data/emp2.csv","r")
# emp_csv=csv.reader(file)
# for emp_list in emp_csv:
#     if (emp_list[2]=='SALESMAN'):
#         print (emp_list[1],emp_list[5],emp_list[2])
# -Pandas를 써서
# import pandas as pd
# emp = pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[ ['ename','sal','job']][ emp['job'] == 'SALESMAN' ]
# print (empresult)
#
# • 문제91. 직업이 SALESMAN,ANALYST인 사원들의 이름과 월급과 직업을 출력
# -Pandas를 쓰지 않고
# import csv
# file=open("D:/data/emp2.csv","r")
# emp_csv=csv.reader(file)
# for emp_list in emp_csv:
#     if emp_list[2] in ['SALESMAN', 'ANALYST']:
#         print (emp_list[1],emp_list[5],emp_list[2])
#
#-Pandas를 써서
# import pandas as pd
# emp = pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[['ename','sal','job']][emp['job'].isin(['SALESMAN','ANALYST'])]
# print (empresult)
#
# • 문제92. 직업이 SALESMAN,ANALYST가 아닌 사원들의 이름과 월급과 직업을 출력
#-pandas를 쓰지 않고
# import csv
#
# for emp in csv.reader(open('C:\data\emp.csv', 'r')):
#     if emp[2] not in ('SALESMAN', 'ANALYST'):
#         print(emp[1], emp[5], emp[2])
# ---------------------------------------------
# import csv
#
# for emp in csv.reader(open('C:\data\emp.csv', 'r')):
#     if (emp[2] != 'SALESMAN') & (emp[2] != 'ANALYST'):  # (  != ) & ( != )  로 해도 됨
# print(emp[1], emp[5], emp[2])
# #-pandas를 써서
#
# import pandas as pd
# emp = pd.DataFrame.from_csv('C:\data\emp.csv')
# empresult = emp[['ename','sal','job']][~emp['job'].isin (['SALESMAN','ANALYST'])]    # not 을 표현할 때는 ~ 붙여주면 됨
# print(empresult)
#
#
# • 문제93. 커미션이 null인 사원들의 이름과 커미션을 출력
#-Pandas를 쓰지 않고
# import csv
# file = open("D:/data/emp_comm.csv",'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#     if emp_list[6] ==None:
#         print (emp_list[1], emp_list[6])
#-Pandas를 떠서
# import pandas as pd
# emp = pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[ ['ename','comm'] ][emp['comm'].isnull()]
# print(empresult)
#
# • 문제94. 커미션이 null이 아닌 사원들의 이름과 커미션을 출력
#-Pandas를 쓰지 않고
# import csv
# file = open("D:/data/emp_comm.csv",'r')
# emp_csv = csv.reader(file)
# for emp_list in emp_csv:
#     if emp_list[6] !=None:
#         print (emp_list[1], emp_list[6])
#-Pandas를 떠서
# import pandas as pd
# emp = pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[ ['ename','comm'] ][~emp['comm'].isnull()]
# print(empresult)
#
#
# • 문제95. 월급이 1000에서 3000 사이인 사원들의 이름과 월급을 출력
# -Pandas를 써서
# import pandas as pd
# emp=pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[ ['ename','sal'] ][(emp['sal'] >= 1000) & (emp['sal'] <= 3000)]
# print(empresult)
#
# -Pandas를 쓰지 않고
# import csv
#
# file=open("D:/data/emp_comm.csv","r")
# emp_csv=csv.reader(file)
# for emp_list in emp_csv:
#     if (int(emp_list[5]) >= 1000) & (int(emp_list[5]) <= 3000):
#         print(emp_list[1],emp_list[5])
#
# • 문제96. 이름의 첫 글자가 S로 시작하는 사원의 이름을 출력
# -Pandas를 써서
# import pandas as pd
# emp=pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[ ['ename','sal'] ][emp['ename'].apply(lambda x:x[0]=='S')]
# print(empresult)
#
# -Pandas를 쓰지 않고
# import csv
#
# file=open("D:/data/emp_comm.csv","r")
# emp_csv=csv.reader(file)
# for emp_list in emp_csv:
#     if emp_list[1][0:1]=='S':
#         print(emp_list[1])
#
# • 문제97. 위 문제를 lambda 표현식을 쓰지 말고 직접 생성해서 실행
# def p97(z) :
#     if z[0] == 'S' :
#         return True
#     return False
#
# import pandas as pd
# emp = pd.DataFrame.from_csv('c:\data\emp2.csv')
# empresult = emp[['ename','sal']][emp['ename'].apply(p97)]
# print(empresult)
#
# • 문제98. 이름이 T로 끝나는 사원 이름, 월급을 출력
# import pandas as pd
# emp=pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp[['ename','sal']][emp['ename'].apply(lambda x:x[-1]=='T')]
# print(empresult)
#
# • 문제99. 직업, 직업별 최대월급을 SALESMAN을 제외하고 출력
# import pandas as pd
# emp=pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = [~emp['job']=='SALESMAN']emp.groupby(['job'])['sal'].max()
# print(empresult)
#
# • 문제100. 부서번호, 직업, 부서번호별 직업별 토탈월급을 pandas로 출력
# import pandas as pd
# emp=pd.DataFrame.from_csv("D:/data/emp.csv")
# empresult = emp.groupby(['deptno','job'])['sal'].sum()
# print(empresult)
#
# • 문제101. JONES보다 더 많이 월급을 받는 사원들의 이름과 월급을 출력
# import pandas as pd
#
# emp=pd.DataFrame.from_csv("D:/data/emp.csv")
# jones=emp[['sal']][emp['ename']=='JONES'].values[0]
# empresult = emp[['ename','sal']][emp['sal'] > jones[0]]  -- 위에서 생성한 jones는 pandas.dataframe 타입이므로 이를 검색 가능하게 바꿔줘야
# print(empresult)                                         -- empresult에서 사용할 수 있다.
#
# • 문제102. SCOTT의 직속 상사 이름을 출력
# import pandas as pd
#
# emp=pd.read_csv("D:/data/emp.csv")
# mgr=emp[['mgr']][emp['ename']=='SCOTT'].values[0]
# #print(mgr)
# empresult = emp[['ename']][emp['empno'] == mgr[0]]
# print(empresult)
#
# • 문제103. 관리자인 사원들의 이름을 출력
# import pandas as pd
#
# emp=pd.read_csv("D:/data/emp.csv")
# mgr=emp[['mgr']]
# empresult = emp[['ename']][emp['empno'].isin (emp['mgr'])]
# print(empresult)
#
# • 문제104. 컬럼 c5, c6, c8이 남아있을 때 어떤 수가 가장 좋은 수인가?
# import pandas as pd
# t_dt = pd.read_csv("d:\data\mit_t.csv")
# result1 = t_dt[(t_dt['PLAYER']==1) & (t_dt['C1'] == 1) & (t_dt['C2'] == 2) & (t_dt['C3'] == 1) &
#                (t_dt['C4'] == 2) & (t_dt['C7'] == 1) & (t_dt['C9'] == 2) &
#                (t_dt['C5'] + t_dt['C6'] + t_dt['C8'] == 1)]
#
# result2 = result1.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max()
#
# result3 = t_dt[(t_dt['LEARNING_ORDER'].isin (result2)) & (t_dt['PLAYER'] == 1)]
#
# a=[]
# for i in result2:
#     a.append(i)
#
# result4 = t_dt[t_dt['LEARNING_ORDER'].isin (a) & (t_dt['PLAYER'] == 1)]
#
# print(result3)
# print('---------------------------------')
# print(result4)
#- result3이랑 result4는 뽑는 결과는 똑같고 result2가 만약 실행 불가능한 데이터타입이 될 경우 a=[]로 따로 리스트화 해서 result4로 돌려준다
#
#
# • 문제105. 딕셔너리 자료형을 이용해서 주어 0, 명사 2, 동사 1로 한글과 영문을 저장
# dic={}
# dic['나는'] = ('I',0)
# dic['소년'] = ('boy',2)
# dic['이다'] = ('am',1)
# dic['피자'] = ('pizza',2)
# dic['먹는다'] = ('eat',1)
# dic
#
# • 문제106. 한글을 입력받아 영어로 번역하게 제작
# dic = {}
# dic['나는'] = ('I', 0)
# dic['소년'] = ('boy', 2)
# dic['이다'] = ('am', 1)
# dic['피자를'] = ('pizza', 2)
# dic['먹는다'] = ('eat', 1)
# result = ''
# input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
# input_list = input_kor.split(' ')
# for i in range(len(input_list)):                    # i : 0                  i : 0
#     for j in input_list:                            # j : 나는            ->  j : 나는
#         if dic[j][1] == i:                          # dic['나는'][1] == 0     dic['소년'][1] == 1
#                                                     # dic['나는'] = ('I', 0)  dic['소년'] = ('boy', 2)
#                                                     #                0   1                   0    1
#
#             result = result + dic[j][0] + ' '
#             #           ''  + dic['나는'][0] + ' '
#
# print(result)
#
# • 문제107. smt_dic 불러오기
# import csv
# file=open("D:/data/smt_dic.csv", "r")
# dic_csv=csv.reader(file)
#     for dic_list in dic_csv:
#         print(dic_list)
#
# • 문제108. smt_dic에서 필요한 것만 뽑아오기
# import csv
# file=open("D:/data/smt_dic.csv", "r")
# dic_csv=csv.reader(file)
# for dic_list in dic_csv:
#         print(dic_list[1], dic_list[3], dic_list[4])
#
# • 문제109. 1번 요소를 key로 하고 3번쨰 요소를 딕셔너리 변수의 0번째 요소로 하고 4번째 요소를 딕셔너리 변수의 4번쨰 요소로 지정해서 딕셔너리에 입력
# import csv
# file=open("D:/data/smt_dic.csv", "r")
# dic_csv=csv.reader(file)
# smt_dic={}
# for dic_list in dic_csv:
#         smt_dic[dic_list[1]] = (dic_list[3], dic_list[4])
# print(smt_dic)
#
# • 문제110. 번역코드와 입력한 딕셔너리를 이용해서 번역기 완성
# import csv
# file=open("D:/data/smt_dic.csv", "r")
# dic_csv=csv.reader(file)
# smt_dic={}
# for dic_list in dic_csv:
#     smt_dic[dic_list[1]] = (dic_list[3], dic_list[4]) # 주어
#     smt_dic[dic_list[2]] = (dic_list[3], dic_list[4]) # 동사
#
# result = ''
# input_kor = input('입력하세요')
# input_list = input_kor.split(' ')
# for i in range(len(input_list)) :
#     for j in input_list :
#         if smt_dic[j][1]==str(i) :
#             result = result + smt_dic[j][0] + ' '
# print(result)
#
# • 문제111. 숫자를 입력받아 짝홀 판단
# a=input('숫자를 입력하세요')
# if int(a) % 2 == 1:
#     print(a,'는 홀수')
# else:
#     print(a,'는 짝수')
#
# • 문제112. mod 함수를 생성
# def mod(a):
#     if a % 2 == 1:
#         return '홀수'
#     else:
#         return '짝수'
#
# print(mod(9983))
#
# • 문제113. 이름을 입력받아 해당사원이 고소득자인지 저소득자인지 판단
# a = input('이름을 입력')
# import pandas as pd
# emp=pd.read_csv("D:/data/emp.csv")
# empresult=emp[['sal']][emp['ename'] == a ].values[0]
# if empresult >= 3000:
#     print('고소득자')
# elif empresult >= 2000:
#     print('적   당')
# else:
#     print('저소득자')#
#--------------------------------------------------------------
# import csv
# file=open("D:/data/emp2.csv", "r")
# emp_csv=csv.reader(file)
# a=input('이름을 입력')
# for i in emp_csv:
#     if (a.upper()==i[2]) & (int(i[5]) >= 3000):
#         print(a,'고소득자')
#     elif (a.upper()==i[2]) & (int(i[5]) >= 2000):
#         print(a,'적당')
#     else:
#         print(a,'저소득자')

#
#  • 문제114. 소문자로 입력해도 되게 바꿈
# a = input('이름을 입력')
# import pandas as pd
# emp=pd.read_csv("D:/data/emp.csv")
# empresult=emp[['sal']][emp['ename'] == a.upper() ].values[0]
# if empresult >= 3000:
#     print('고소득자')
# elif empresult >= 2000:
#     print('적   당')
# else:
#     print('저소득자')
#
#  • 문제115,116. 가우스공식
# a = int(input('숫자1 입력'))
# b = int(input('숫자2 입력'))
# if a>b:
#     print((a+b)/2*(a-b+1))
# elif b>a:
#     print((b+a)/2*(b-a+1))
#
#  • 문제117. 구구단 출력
# for i in range(2,10):
#     print('---------',i,'단----------')
#     for j in range(1,10):
#         print(i,' X ',j,' = ',i*j)
#     print('------------------------')
#
#  • 문제118. 별 출력
# for i in range(1, 10):
#     for j in range(i):
#         print('★', end="")
#     print()
#
# for i in range(1, 11):
#     print('*' * i)
#
#  • 문제119. 별 출력 반대로
# for i in range(10,0,-1):
#     for j in range(i):
#         print('★', end = "")
#     print()
#
# for i in range(10,0,-1):
#     print('*'*i)
#
#  • 문제120. 파일런
#for i in range(1,6):
#         print(' '*(12-i),'★'*i)
# for i in range(4,0,-1):
#         print(' '*(12-i),'★'*i)
#
#  • 문제121. 5*5 별
# a = int(input('가로'))
# b = int(input('세로'))
# for i in range(a):
#    for i in range(b):
#         c='★'*a
#    print(c)
# --------------------------
# a = int(input('가로'))
# b = int(input('세로'))
# for i in range(b):
#     result=''
#     for i in range(a):
#         result +='★'
#     print(result)
#
#  • 문제122. 구구단 가로로
# for i in range(1,10):
#     r=''
#     for j in range(2,10):
#         r += (str(j)+' X '+str(i)+' = '+str(j*i)+'').ljust(13)
#     print(r)
#
#  • 문제123. for loop문을 이용해서 power 함수를 구현
# a = int(input('밑수'))
# b = int(input('지수'))
# for i in range(a):
#     c = 1
#     for i in range(b):
#         c = c*a
#
# print(c)
#
#  • 문제124.겨울왕국 대본에는 숫자가 몇개 있는가?
# winter = open('C:\data\winter.txt')
# lines = winter.readlines()
# total = 0
#
# for s in lines:
#     total += sum(i.isdigit() for i in s)
# print(total)
#
# • 문제125.공백, 알파벳, 숫자도 아닌 특수문자 몇개 포함되어있는지 확인
# winter = open('C:\data\winter.txt')
# lines = winter.readlines()
# digit = 0
# alpha = 0
# space = 0
# total = 0
# for s in lines:
#     alpha += sum(i.isalpha() for i in s)
#     digit += sum(i.isdigit() for i in s)
#     space += sum(i.isspace() for i in s)
#     total += len(s)
# print(total - alpha - digit - space)
#
#  • 문제126.숫자 물어보게 하고 숫자 입력하면 해당 숫자만큼 아래 그림 그려지게
# a = int(input('몇 줄 ? '))
# cnt = 0
# while cnt < a:
#     cnt = cnt + 1
#     result = '★' * cnt
#     blank = ' ' * (a - cnt)
#     print(blank + result)
#
#  • 문제127.팩토리얼을 while loop 문으로 구현 a = int(input('팩토리얼 숫자 '))
# result = 1
#
# while a >= 1:
#     result *= a
#     a -= 1
# print(result)
#
#  • 문제128.로그함수 파이썬으로 구현 밑수 입력 2 진수 입력 16 로그값은 4 입니다.
#
# a = int(input('밑수 '))
# b = int(input('진수 '))
# cnt = 0
#
# while b >= a:
#     b /= a
#     cnt += 1
#
# print('\n로그값은', cnt, '입니다.')
#
#  • 문제129.두수 입력받아서 최대공약수 구하기( while loop 랑 유클리드 호제법 수행) 첫번째 수 입력 두번째 수 입력
#
# first = int(input('첫번째 수 '))
# second = int(input('두번째 수 '))
# mod = 1
# result = 0
# while mod != 0:
#     mod = first % second
#     result = second
#     first, second = second, mod
# print(result)
#
#  • 문제130.최대공약수 알고싶은 두 수 입력
# a = input('두 수 입력 ')
#
# a_list = a.split(' ')
# first = int(a_list[0])
# second = int(a_list[1])
# mod = 1
# result = 0
#
# while mod != 0:
#     mod = first % second
#     result = second
#     first, second = second, mod
# print(result)
#
# • 문제131. 1부터 10까지 5를 제외하고 출력
# num = 0
# while num < 10:
#     num += 1
#     if num == 5:
#         continue
#     print(num)
#
# 문제132 함수를 생성하는데 아래와 같이 숫자를 넣어서 실행하면 해당 숫자만큼 숫자가 세로로 출력!
#
# print(break_fun(10))  # 10이 loop문을 중단시킬 숫자
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
#
# 문제133 위의 함수를 수정해서 결과가 가로로 출력!
#
# print(break_fun(10))  # 10이 loop 문을 중단시킬 숫자
#
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
#
##
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
#
# 문제139 emp.csv 와 dept.csv를 각각 읽어서 emp_dic, dept, dic딕셔너리 자료형으로 만드는 스크립트를 하나로 합치시오
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

#     문제143 pandas를 이용해서 ename, loc 출력!
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

#
#     문제144 부서위치가 DALLAS인 사원들의 이름과 부서위치 출력!
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
# 문제149 아래와 같이 이름만 넣으면 소속팀과 직위가 출력되는 함수를 생성
# def f_149(name, team='머신러닝팀', position):
#     print('이름 = ', name)
#     print('소속팀 = ', team)
#     print('직위 = ', position)         #문자열.format() `

#
# 문제150
#
#
# 문제151 아래와 같이 숫자를 입력하고 함수를 실행하면 숫자가 세로로 출력되게
#def print_a(*s):
#     for i in s:
#         print(i)
#
# print_a(1,2,3,4,5)
#
# 문제152 아래 스크립트에서 마지막 scope_test()를 실행했을 떄 a가 1이 아니라 0이 출력되게 하려면 scope_test() 함수를 생성할 때 어떻게 생성해야하는가
# def scope_test():
#     a = 1
#     print('a : {0}'.format(a))
#
#
# scope_test()
#
# a=0
#
# scope_test()
#--------------------------------
#def scope_test():
#     global a
#     a = 1
#     print('a : {0}'.format(a))
# scope_test()
# print('-----------')
# a=0
# print('a : {0}'.format(a))
# print('-----------')
# scope_test()
#
# 문제153. 10!을 재귀함수로 구현해서 출력
# def fac(n):
#     if n == 0:
#         return 1
#     elif n > 0:
#         return fac(n-1)*n
#
# print(fac(10))
# #fac(10)
#
# 문제154. 16과 20의 최대공약수를 재귀함수로 출력
# def gcdtwo(a,b):
#     if min(a,b) == 0:
#         return max(a,b)
#     return gcdtwo(b,a%b)
#
# 문제155. 가변 매개변수와 재귀 알고리즘을 이용해서 최대 공약수를 출력하는 함수 생성



• 문제160.표준편차를 출력하는 함수를 모듈화 시켜서 다른 실행창에서 실행


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
