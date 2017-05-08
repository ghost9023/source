# # [['327', '2', '0'], ['123', '1', '1'], ['356', '1', '0'], ['489', '0', '1']]
#
#
# # 128, 138, 158, 168, 178, 218, 238, 258, 268, 278, 318, 328, 358, 368, 378, 518, 528, 538, 568, 578, 618, 628, 638, 658, 678, 718, 728, 738, 758, 768,
# # 812, 813, 815, 816, 817, 821, 823, 825, 826, 827, 831, 832, 835, 836, 837, 851, 852, 853, 856, 857, 861, 862, 863, 865, 867, 871, 872, 873, 875, 876
#
# elif (int(a2[j][1]) == 0) & (int(a2[j][2]) == 1):  # 0스트 1볼
# for k in anslist:
#     if (str(k)[0] == a2[j][0][1]) & (str(k)[2] != a2[j][0][0]) & (str(k)[2] != a2[j][0][1]) & (
#         str(k)[2] != a2[j][0][2]) & (str(k)[1] != a2[j][0][0]) & (str(k)[1] != a2[j][0][1]) & (
#         str(k)[1] != a2[j][0][2]):
#         ans.append(k)
#     if (str(k)[0] == a2[j][0][2]) & (str(k)[2] != a2[j][0][0]) & (str(k)[2] != a2[j][0][1]) & (
#         str(k)[2] != a2[j][0][2]) & (str(k)[0] != a2[j][0][0]) & (str(k)[0] != a2[j][0][1]) & (
#         str(k)[0] != a2[j][0][2]):
#         ans.append(k)
#     if (str(k)[1] == a2[j][0][0]) & (str(k)[0] != a2[j][0][0]) & (str(k)[0] != a2[j][0][1]) & (
#         str(k)[0] != a2[j][0][2]) & (str(k)[1] != a2[j][0][0]) & (str(k)[1] != a2[j][0][1]) & (
#         str(k)[1] != a2[j][0][2]):
#         ans.append(k)
#     if (str(k)[1] == a2[j][0][2]) & (str(k)[2] != a2[j][0][0]) & (str(k)[2] != a2[j][0][1]) & (
#         str(k)[2] != a2[j][0][2]) & (str(k)[1] != a2[j][0][0]) & (str(k)[1] != a2[j][0][1]) & (
#         str(k)[1] != a2[j][0][2]):
#         ans.append(k)
#     if (str(k)[2] == a2[j][0][0]) & (str(k)[2] != a2[j][0][0]) & (str(k)[2] != a2[j][0][1]) & (
#         str(k)[2] != a2[j][0][2]) & (str(k)[0] != a2[j][0][0]) & (str(k)[0] != a2[j][0][1]) & (
#         str(k)[0] != a2[j][0][2]):
#         ans.append(k)
#     if (str(k)[2] == a2[j][0][1]) & (str(k)[0] != a2[j][0][0]) & (str(k)[0] != a2[j][0][1]) & (
#         str(k)[0] != a2[j][0][2]) & (str(k)[1] != a2[j][0][0]) & (str(k)[1] != a2[j][0][1]) & (
#         str(k)[1] != a2[j][0][2]):
#         ans.append(k)
#
#
#
# # _ 4 _ str(k)[0] str(k)[0] str(k)[2] str(k)[2]
# if (a2[j][0][0] == str(k)[1]) & (a2[j][0][0] != str(k)[0]) & (a2[j][0][2] != str(k)[0]) & (a2[j][0][0] != str(k)[2]) & (a2[j][0][2] != str(k)[2]):
#     ans.append(k)
# # _ _ 4 str(k)[0] str(k)[0] str(k)[1] str(k)[1]
# if (a2[j][0][0] == str(k)[2]) & (a2[j][0][0] != str(k)[0]) & (a2[j][0][1] != str(k)[0]) & (a2[j][0][0] != str(k)[1]) & (a2[j][0][1] != str(k)[1]):
#     ans.append(k)
# # 8 _ _ str(k)[1] str(k)[1] str(k)[2] str(k)[2]
# if (a2[j][0][1] == str(k)[0]) & (a2[j][0][1] != str(k)[1]) & (a2[j][0][2] != str(k)[1]) & (a2[j][0][1] != str(k)[2]) & (a2[j][0][2] != str(k)[2]):
#     ans.append(k)
# # _ _ 8 str(k)[0] str(k)[0] str(k)[1] str(k)[1]
# if (a2[j][0][1] == str(k)[2]) & (a2[j][0][0] != str(k)[0]) & (a2[j][0][1] != str(k)[0]) & (a2[j][0][0] != str(k)[1]) & (a2[j][0][1] != str(k)[1]):
#     ans.append(k)
# # 9 _ _ str(k)[1] str(k)[1] str(k)[2] str(k)[2]
# if (a2[j][0][2] == str(k)[0]) & (a2[j][0][1] != str(k)[1]) & (a2[j][0][2] != str(k)[1]) & (a2[j][0][1] != str(k)[2]) & (a2[j][0][2] != str(k)[2]):
#     ans.append(k)
# # _ 9 _ str(k)[0] str(k)[0] str(k)[2] str(k)[2]
# if (a2[j][0][2] == str(k)[1]) & (a2[j][0][0] != str(k)[0]) & (a2[j][0][2] != str(k)[0]) & (a2[j][0][0] != str(k)[2]) & (a2[j][0][2] != str(k)[2]):
#     ans.append(k)
#
#
# import os, psutil
#
# # 시작 메모리 체크
# proc1 = psutil.Process(os.getpid())
# mem1 = proc1.memory_info()
# before_start=mem1[0]
#
# # 코드 실행
#
# # 실행 후 맨 밑에서 코드 구동 후 메모리 체크
# proc = psutil.Process(os.getpid())
# mem = proc.memory_info()
# after_start=mem[0]
# print('memory use : ',after_start-before_start)

##############################################################
from operator import itemgetter

question_list = []

count = 0
n = int(input())
while count < n:
    count = count+1
    question_input = list(input().split(' '))
    question_list.append(question_input)
list.sort(question_list, key=itemgetter(1), reverse=True)
answer_list=[]

for k in range(122,988,1):
    if (int(str(k)[1]) != 0) & (int(str(k)[2]) != 0) & (str(k)[0] != str(k)[1]) & (str(k)[0] != str(k)[2]) & (str(k)[1] != str(k)[2]):
        answer_list.append(k)

case=[]

for j in range(0,len(question_list),1):
    if (int(question_list[j][1]) == 3) & (int(question_list[j][2]) == 0):
        case.append(question_list[j][0])
        break
    elif (int(question_list[j][1]) == 0) & (int(question_list[j][2]) == 0):
        for k in answer_list:
            if (str(k)[0] != question_list[j][0][0]) & (str(k)[0] != question_list[j][0][1]) & (str(k)[0] != question_list[j][0][2]) \
                    & (str(k)[1] != question_list[j][0][0]) & (str(k)[1] != question_list[j][0][1]) & (str(k)[1] != question_list[j][0][2]) \
                    & (str(k)[2] != question_list[j][0][0]) & (str(k)[2] != question_list[j][0][1]) & (str(k)[2] != question_list[j][0][2]) :
                case.append(k)

    elif (int(question_list[j][1]) == 2) & (int(question_list[j][2]) == 0):
        for k in answer_list:
            if (str(k)[0] == question_list[j][0][0]) & (str(k)[1] == question_list[j][0][1]) & (str(k)[2] != question_list[j][0][2]):
                case.append(k)
            if (str(k)[0] == question_list[j][0][0]) & (str(k)[1] != question_list[j][0][1]) & (str(k)[2] == question_list[j][0][2]):
                case.append(k)
            if (str(k)[0] != question_list[j][0][0]) & (str(k)[1] == question_list[j][0][1]) & (str(k)[2] == question_list[j][0][2]):
                case.append(k)

    elif (int(question_list[j][1]) == 1) & (int(question_list[j][2]) == 0):
        for k in answer_list:
            if (str(k)[0] == question_list[j][0][0]) & (str(k)[1] != question_list[j][0][1]) \
                    & (str(k)[2] != question_list[j][0][2]) & (str(k)[2] != question_list[j][0][0])\
                    & (str(k)[2] != question_list[j][0][1]) & (str(k)[2] != question_list[j][0][2]) & (str(k)[1] != question_list[j][0][0]) \
                    & (str(k)[1] != question_list[j][0][1]) & (str(k)[1] != question_list[j][0][2]):
                case.append(k)
            if (str(k)[0] != question_list[j][0][0]) & (str(k)[1] == question_list[j][0][1]) \
                    & (str(k)[2] != question_list[j][0][2]) & (str(k)[2] != question_list[j][0][0]) \
                    & (str(k)[2] != question_list[j][0][1]) & (str(k)[2] != question_list[j][0][2]) \
                    & (str(k)[0] != question_list[j][0][0]) & (str(k)[0] != question_list[j][0][1]) \
                    & (str(k)[0] != question_list[j][0][2]):
                case.append(k)
            if (str(k)[0] != question_list[j][0][0]) & (str(k)[1] != question_list[j][0][1]) \
                    & (str(k)[2] == question_list[j][0][2]) & (str(k)[0] != question_list[j][0][0]) \
                    & (str(k)[0] != question_list[j][0][1]) & (str(k)[0] != question_list[j][0][2]) \
                    & (str(k)[1] != question_list[j][0][0]) & (str(k)[1] != question_list[j][0][1]) \
                    & (str(k)[1] != question_list[j][0][2]):
                case.append(k)



    elif (int(question_list[j][1]) == 1) & (int(question_list[j][2]) == 1):
        for k in answer_list:
            if (str(k)[0] == question_list[j][0][0]) & (str(k)[2] == question_list[j][0][1]) & (str(k)[1] != question_list[j][0][2]):
                case.append(k)
            if (str(k)[0] == question_list[j][0][0]) & (str(k)[1] == question_list[j][0][2]) & (str(k)[2] != question_list[j][0][1]):
                case.append(k)
            if (str(k)[1] == question_list[j][0][1]) & (str(k)[0] == question_list[j][0][2]) & (str(k)[2] != question_list[j][0][0]):
                case.append(k)
            if (str(k)[1] == question_list[j][0][1]) & (str(k)[2] == question_list[j][0][0]) & (str(k)[0] != question_list[j][0][2]):
                case.append(k)
            if (str(k)[2] == question_list[j][0][2]) & (str(k)[1] == question_list[j][0][0]) & (str(k)[0] != question_list[j][0][1]):
                case.append(k)
            if (str(k)[2] == question_list[j][0][2]) & (str(k)[0] == question_list[j][0][1]) & (str(k)[1] != question_list[j][0][0]):
                case.append(k)

    elif (int(question_list[j][1]) == 1) & (int(question_list[j][2]) == 2):
        for k in answer_list:
            if (str(k)[0] == question_list[j][0][0]) & (str(k)[1] == question_list[j][0][2]) & (str(k)[2] == question_list[j][0][1]):
                case.append(k)
            if (str(k)[1] == question_list[j][0][1]) & (str(k)[0] == question_list[j][0][2]) & (str(k)[2] == question_list[j][0][0]):
                case.append(k)
            if (str(k)[2] == question_list[j][0][2]) & (str(k)[1] == question_list[j][0][0]) & (str(k)[0] == question_list[j][0][1]):
                case.append(k)

    elif (int(question_list[j][1]) == 0) & (int(question_list[j][2]) == 2):
        for k in answer_list:
            if (str(k)[0] == question_list[j][0][1]) & (str(k)[1] == question_list[j][0][0]) & (str(k)[2] != question_list[j][0][2]):
                case.append(k)
            if (str(k)[0] == question_list[j][0][2]) & (str(k)[2] == question_list[j][0][0]) & (str(k)[1] != question_list[j][0][1]):
                case.append(k)
            if (str(k)[1] == question_list[j][0][2]) & (str(k)[2] == question_list[j][0][1]) & (str(k)[0] != question_list[j][0][0]):
                case.append(k)


    elif (int(question_list[j][1]) == 0) & (int(question_list[j][2]) == 1):
        for k in answer_list:

            if (question_list[j][0][0] == str(k)[1]) & (question_list[j][0][0] != str(k)[0]) \
                    & (question_list[j][0][2] != str(k)[0]) & (question_list[j][0][0] != str(k)[2]) & (question_list[j][0][2] != str(k)[2]):
                case.append(k)

            if (question_list[j][0][0] == str(k)[2]) & (question_list[j][0][0] != str(k)[0]) \
                    & (question_list[j][0][1] != str(k)[0]) & (question_list[j][0][0] != str(k)[1]) & (question_list[j][0][1] != str(k)[1]):
                case.append(k)

            if (question_list[j][0][1] == str(k)[0]) & (question_list[j][0][1] != str(k)[1]) \
                    & (question_list[j][0][2] != str(k)[1]) & (question_list[j][0][1] != str(k)[2]) & (question_list[j][0][2] != str(k)[2]):
                case.append(k)

            if (question_list[j][0][1] == str(k)[2]) & (question_list[j][0][0] != str(k)[0]) \
                    & (question_list[j][0][1] != str(k)[0]) & (question_list[j][0][0] != str(k)[1]) & (question_list[j][0][1] != str(k)[1]):
                case.append(k)

            if (question_list[j][0][2] == str(k)[0]) & (question_list[j][0][1] != str(k)[1]) \
                    & (question_list[j][0][2] != str(k)[1]) & (question_list[j][0][1] != str(k)[2]) & (question_list[j][0][2] != str(k)[2]):
                case.append(k)

            if (question_list[j][0][2] == str(k)[1]) & (question_list[j][0][0] != str(k)[0]) \
                    & (question_list[j][0][2] != str(k)[0]) & (question_list[j][0][0] != str(k)[2]) & (question_list[j][0][2] != str(k)[2]):
                case.append(k)

    elif (int(question_list[j][1]) == 0) & (int(question_list[j][2]) == 3):
        for k in answer_list:
            if (str(k)[0] == question_list[j][0][1]) & (str(k)[1] == question_list[j][0][2]) & (str(k)[2] != question_list[j][0][0]):
                case.append(k)
            if (str(k)[0] == question_list[j][0][2]) & (str(k)[1] != question_list[j][0][0]) & (str(k)[2] == question_list[j][0][1]):
                case.append(k)


final_answer = [i for i in set(case) if case.count(i) >= len(question_list)]
result = len(final_answer)
print(result)

# 질문갯수 : 4
# 숫자3자리 스트라이크 볼넷을 입력 123 1 1
# 숫자3자리 스트라이크 볼넷을 입력 356 1 0
# 숫자3자리 스트라이크 볼넷을 입력 327 2 0
# 숫자3자리 스트라이크 볼넷을 입력 489 0 1
# 정답의 개수 :  2