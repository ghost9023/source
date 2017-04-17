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
#     return '짝수'
# print (odd_even(a))
#
# • 문제42. power 함수를 이용해서 숫자를 입력 받아 지수를 계산
# a = int(input('밑수를 입력'))
# b = int(input('지수를 입력'))
# import math
# math.pow(a, b)
#
# • 문제43. 오늘부터 3달 뒤의 날짜를 출력
# import datetime
# today = datetime.date.today()
# print(today)