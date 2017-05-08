import math
import random

a2 = []  # 데이터를 받을 리스트

count = 0
n = int(input('질문갯수 : '))   # 질문 갯수 입력
while count < n:
    count = count+1
    a1 = list(input('숫자3자리 스트라이크 볼넷을 입력').split(' '))       # 질문을 입력받아 리스트 형태로 저장
    a2.append(a1)

ans = []

for k in range(122,988,1):
    for j in range(0,len(a2),1):
        if (int(a2[j][1]) == 3) & (int(a2[j][2]) == 0):
            ans.append(k)
            break

        elif (int(a2[j][1]) == 2) & (int(a2[j][2]) == 0):
            if (str(k)[0] == a2[j][0]) & (str(k)[1] == a2[j][1]) & (str(k)[2] != a2[j][2]):
                ans.append(k)
            if (str(k)[0] == a2[j][0]) & (str(k)[1] != a2[j][1]) & (str(k)[2] == a2[j][2]):
                ans.append(k)
            if (str(k)[0] != a2[j][0]) & (str(i)[1] == a2[j][1]) & (str(k)[2] == a2[j][2]):
                ans.append(k)
            break

        elif (int(a2[j][1]) == 1) & (int(a2[j][2]) == 0):
            if (str(k)[0] == a2[j][0]) & (str(k)[1] == a2[j][1]) & (str(k)[2] != a2[j][2]):
                ans.append(k)
            if (str(k)[0] == a2[j][0]) & (str(k)[1] != a2[j][1]) & (str(k)[2] == a2[j][2]):
                ans.append(k)
            if (str(k)[0] != a2[j][0]) & (str(i)[1] == a2[j][1]) & (str(k)[2] == a2[j][2]):
                ans.append(k)

        elif (int(a2[j][1]) == 1) & (int(a2[j][2]) == 1):

        elif (int(a2[j][1]) == 1) & (int(a2[j][2]) == 2):

        elif (int(a2[j][1]) == 0) & (int(a2[j][2]) == 0):

        elif (int(a2[j][1]) == 0) & (int(a2[j][2]) == 1):

        elif (int(a2[j][1]) == 0) & (int(a2[j][2]) == 2):

        elif (int(a2[i][1]) == 0) & (int(a2[i][2]) == 3):






# if len(a2) == 1:  # 질문의 갯수가 1일 때
#     if (int(a2[0][1]) + int(a2[0][2]))==0:
#         a3 = a3-3
#         print('가능한 답의 경우의 수는 ', math.factorial(a3), ' 입니다.')
#     elif (int(a2[0][1]) + int(a2[0][2])) == 1:
#         a3 = a3-2
#         if int(a2[0][1]) == 1:
#             print('가능한 답의 경우의 수는 ', 3*a3*(a3-1)*(a3-2), ' 입니다.')
#         if int(a2[0][2]) == 1:
#             print('가능한 답의 경우의 수는 ', math.factorial(3) * a3 * (a3 - 1) * (a3 - 2), ' 입니다.')
#     elif (int(a2[0][1]) + int(a2[0][2])) == 2:
#         a3 = a3-1
#         print('가능한 답의 경우의 수는 ', math.factorial(3) * a3 * (a3 - 1) * (a3 - 2), ' 입니다.')
#     elif (int(a2[0][1]) + int(a2[0][2])) == 3:
#         a3 = a3
#         if int(a2[0][1]) == 3:
#             print('가능한 답의 경우의 수는 3 입니다.')
#         elif (int(a2[0][1]) == 1) & (int(a2[0][2]) == 2):
#             print('가능한 답의 경우의 수는 ', math.factorial(3) * a3 * (a3 - 1) * (a3 - 2), ' 입니다.')
#         elif int(a2[0][2]) == 3:
#             print('가능한 답의 경우의 수는 ', math.factorial(3) * a3 * (a3 - 1) * (a3 - 2), ' 입니다.')
