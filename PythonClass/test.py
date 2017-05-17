#산점도, 상관계수
#임산부의 에스트리올 수치가 출생시 체중에 미치는 영향?
import matplotlib.pyplot as plt #산점도 그리기 위한 모듈
import numpy as np
#a : 에스트리올 수치 / b : 출생시 체중
a = np.array([7,9,9,12,14,16,16,14,16,16,17,19,21,24,15,16,17,25,27,15,15,15,16,19,18,17,18,20,22,25,24])
b = np.array([25,25,25,27,27,27,24,30,30,31,30,31,30,28,32,32,32,32,34,34,34,35,35,34,35,36,37,38,40,39,43])
plt.plot(a, b, 'bo') #산점도 그리
plt.show()
print(np.corrcoef(a,b)) #상관계수
#|r| 0~0.4 약한 상관관계,  0.4~0.75 중간 상관관계, 0.75~1 강한 상관관계]