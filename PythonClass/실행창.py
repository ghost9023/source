def gcdtwo(a,b):                    # 두 수의 최대공약수를 출력
                                    # 분모가 0일경우 에러가 발생하므로 0인 경우를 따로 생각
    if min(a,b) == 0:               # 0과 A의 최대공약수는 무조건 A 이기 떄문에
        return max(a,b)             # 두 수중 최소값이 0인경우 두 수중 맥스값으로 최대공약수 출력
    return gcdtwo(b,a%b)            # 0이 아닌경우에 대해 유클리드호제법으로 재귀

def gcd(a):                         # 여러 수 중에서 최대공약수를 출력하는 알고리즘
    b=gcdtwo(max(a),min(a))         # 여러 수 중 두수를 뽑아서 최대공약수를 구하고
                                    # 다른 두수를 뽑아서 최대공약수를 구하고를 반복해서
    a.remove(min(a))                # 마지막에 남는 최대공약수가 전체의 최대공약수인 점을 이용
    a.remove(max(a))                # 정렬할 필요가 없게 전체 수에서 최대, 최소값을 뽑아서
                                    # 최대공약수를 구하는데 계산에 사용한 수는 제거하고
    a.append(b)                     # 위에서 구한 최대공약수를 리스트에 추가
    if max(a)==min(a):              # 위 과정을 재귀를 통해 반복하면 최대공약수만 2개 남는데
        print('최대공약수는 : ',a[0])  # 그경우에서 재귀를 종료하고 최대공약수를 출력
    else:
        gcd(a)


def list(*n):                       # 가변 매개변수로 데이터를 여러개 입력받으면
                                    # 튜플 형태이기 때문에 데이터 변경이 불가능
    a = []                          # 리스트를 생성하고 데이터 변경이 가능하도록
    for i in n:                     # 튜플 데이터를 잘라서 리스트에 입력
        a.append(i)
    gcd(a)                          # 최종적으로 생성한 리스트 변수를
                                    # 위에 생성한 최대공약수 함수에 입력해서 최대공약수 계산


# 사용 예

######################## 결과 값 ########################
# list(128,116,80,64,24,6)
# K:\Python\envVirtual\Scripts\python.exe K:/Python/source/PythonClass/실행창.py
# 최대공약수는 :  2
#
# Process finished with exit code 0

# list(1000, 500, 250, 100, 25, 25)
# K:\Python\envVirtual\Scripts\python.exe K:/Python/source/PythonClass/실행창.py
# 최대공약수는 :  25
#
# Process finished with exit code 0

# list(10000, 10000, 2000, 550, 102000, 195302, 9508234, 1816, 33154)
# K:\Python\envVirtual\Scripts\python.exe K:/Python/source/PythonClass/실행창.py
# 최대공약수는 :  2
#
# Process finished with exit code 0
