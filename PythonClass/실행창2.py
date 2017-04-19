import csv
file=open("D:/data/smt_dic.csv", "r")
dic_csv=csv.reader(file)
smt_dic={}
for dic_list in dic_csv:
    smt_dic[dic_list[1]] = (dic_list[3], dic_list[4])
    smt_dic[dic_list[2]] = (dic_list[3], dic_list[4])

result = ''
input_kor = input('입력하세요')
input_list = input_kor.split(' ')
for i in range(len(input_list)) :
    for j in input_list :
        if smt_dic[j][1]==str(i) :
            result = result + smt_dic[j][0] + ' '
print(result)

# dic = {}
# dic['나는'] = ('I', 0)
# dic['소년'] = ('boy', 2)
# dic['이다'] = ('am', 1)
# dic['피자를'] = ('pizza', 2)
# dic['먹는다'] = ('eat', 1)
# result = ''
# input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
# input_list = input_kor.split(' ')
# for i in range(len(input_list)) :
#     for j in input_list :
#         if dic[j][1]==i :
#             result = result + dic[j][0] + ' '
# print(result)
# print(dic)