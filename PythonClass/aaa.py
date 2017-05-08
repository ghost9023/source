inputs = []

inputss=[['남','30대','no','yes','no','no'],
            ['여','20대','yes','yes','yes','no'],
            ['여','20대','yes','yes','no','no'],
            ['여','40대','no','no','no','no'],
            ['여','30대','no','yes','no','no'],
            ['여','30대','no','no','yes','no'],
            ['여','20대','no','yes','no','no'],
            ['여','20대','no','yes','yes','yes'],
            ['여','30대','yes','yes','no','yes'],
            ['남','40대','yes','no','yes','no'],
            ['남','20대','no','no','no','no'],
            ['남','30대','no','yes','yes','no'],
            ['남','20대','yes','no','no','no'],
            ['여','30대','yes','yes','no','yes'],
            ['남','30대','yes','yes','yes','yes'],
            ['여','30대','yes','no','no','no'],
            ['여','30대','no','yes','yes','yes'],
            ['남','20대','yes','yes','no','no'],
            ['남','40대','yes','no','yes','no'],
            ['남','30대','no','no','no','no'],
            ['여','30대','yes','yes','no','yes'],
            ['남','30대','yes','no','yes','no'],
            ['여','40대','no','yes','yes','yes'],
            ['남','30대','no','yes','no','no'],
            ['여','30대','yes','yes','yes','yes'],
            ['여','40대','yes','no','yes','no'],
            ['남','40대','yes','yes','no','yes'],
            ['여','40대','yes','yes','no','yes']]

labelss = ['gender', 'age', 'job_yn', 'marry_yn', 'car_yn', 'coupon_yn']

for data in inputss:
    temp_dict = {}
    for i in range(len(labelss)):
        if i != 5:
            temp_dict[labelss[i]] = data[i]
    inputs.append(tuple((temp_dict, True if data[5] == 'yes' else False)))

print(inputs)
# print(createdataset())
#
# dict={}
# inputs=['여','20대','yes','yes','yes','no']
# labels=['gender','age','job_yn','marry_yn','car_yn','coupon_yn']
# for i in range(len(labels)):
#     dict[labels[i]] = inputs[i]