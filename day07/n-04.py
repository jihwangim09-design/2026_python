import numpy as np
# 1차원 배열 통계 함수
x = np.array( [1,2,3,4,5] )
print( np.min(x) , np.max(x)) # 최솟값 , 최댓값 # 1 5
print( np.argmin(x) , np.argmax(x)) # 최솟값위치 , 최댓값위치 # 0 4
print( np.sum(x) , np.mean(x) , np.median(x) ) # 합계 , 평균 , 중앙값 # 15 3.0 3.0
print( np.var(x) ) #분산 : 평균으로부터 요소 값들이 떨어진 정도 # 2.0
print( np.std(x) ) #표준편차 : 분산에 양의 제곱근 사용하여 데이터 단위 맞춘 값 # 1.414213562373095
print( np.sqrt(x) ) #양의제곱근(루트) # [1.         1.41421356 1.73205081 2.         2.23606798]




