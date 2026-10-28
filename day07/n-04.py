import numpy as np
# Python NumPy Practice2
# [기본 제공 코드] CSV 파일 로드 (헤더 제외, 콤마 구분)
data = np.genfromtxt('./day07/customer_purchase_data.csv', delimiter=',', skip_header=1)
# 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
print(f"데이터 형태: {data.shape}")


# 1차원 배열 통계 함수
x = np.array( [1,2,3,4,5] )
print( np.min(x) , np.max(x)) # 최솟값 , 최댓값 # 1 5
print( np.argmin(x) , np.argmax(x)) # 최솟값위치 , 최댓값위치 # 0 4
print( np.sum(x) , np.mean(x) , np.median(x) ) # 합계 , 평균 , 중앙값 # 15 3.0 3.0
print( np.var(x) ) #분산 : 평균으로부터 요소 값들이 떨어진 정도 # 2.0
print( np.std(x) ) #표준편차 : 분산에 양의 제곱근 사용하여 데이터 단위 맞춘 값 # 1.414213562373095
print( np.sqrt(x) ) #양의제곱근(루트) # [1.         1.41421356 1.73205081 2.         2.23606798]
# 2차원 배열 통계 함수
# np.통계함수( 2차원배열 , axis = 생략시1차원평탄화,0열마다,1행마다)
y = np.array( [ [1,2,3] , [4,5,6] ])
print( np.min(y) , np.max(y)) #배열내 최솟값과 최댓값# 1 6
print( np.min(y , axis= 0) , np.max( y , axis= 1) ) # axis = 0 열마다 = 1 행단위 # [1 2 3] [3 6]
print( np.argmin(y) , np.argmax(y)) # 최솟값과 최댓값의 위치(인덱스)추출 # 0 5
print( np.sum( y, axis=0) , np.mean( y,axis=0) , np.median( y, axis=1) ) # 합계,평균,중앙값(대푯값)# [5 7 9] [2.5 3.5 4.5] [2. 5.]



