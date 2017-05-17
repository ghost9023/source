# 수 계산에 사용할 조건인 승리(end) 조건을 담는 부분
end=[]


# 가로 직선5
for a in range(0,5,1):
    for b in range(a,a+73,9):
        end.append(tuple([b,b+1,b+2,b+3,b+4]))
# print(len(end))

# 세로 직선5
for c in range(0,45,1):
    end.append(tuple([c,c+9,c+18,c+27,c+36]))
# print(len(end))

# 대각선 ↘5
for d in range(0,37,9):
    for e in range(d,d+5,1):
        end.append(tuple([e,e+10,e+20,e+30,e+40]))
# print(len(end))

# 대각선 ↙5
for i in range(4,41,9):
    for j in range(i,i+5,1):
        end.append(tuple([j,j+8,j+16,j+24,j+32]))
print(end)