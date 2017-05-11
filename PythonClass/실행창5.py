
end=[]

# 가로 직선
for a in range(0,5,1):
    for b in range(a,a+72,9):
        end.append(tuple([b,b+1,b+2,b+3,b+4]))


# 세로 직선
for c in range(0,45,1):
    end.append(tuple([c,c+9,c+18,c+27,c+36]))


# 대각선 ↘
for d in range(0,37,9):
    for e in range(d,d+5,1):
        end.append(tuple([e,e+10,e+20,e+30,e+40]))

# 대각선 ↙
for f in range(4,41,1):
    for g in range(f,f+5,1):
        end.append(tuple([g,g+8,g+16,g+24,g+32]))

print(end)
