# a=int(input('첫수'))           #16
# b=int(input('두수'))           #8
#
# while a != b:
#     if a > b:
#         a = a-b
#     else:
#         b = b-a
# print(a)

c=input('첫수, 두수 공백넣어서 입력')
d=c.split(' ')
aa=int(d[0])
bb=int(d[1])
while aa != bb:
    if aa > bb:
        aa = aa-bb
    else:
        bb = bb-aa
print(aa)