# 1] 항 추가 하는 함수
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures()      # 객체 생성
poly.fit([[ 2 ]])                # 특성(2) 규칙
print(poly.transform( [[ 2 ]]) ) # 2일때 [[1. 2. 4.]] 3일때 [[1. 3. 9.]] 기본절편,원래값,제곱값
# 2] 기본 절편 제외 # include_bias= False
poly = PolynomialFeatures( include_bias= False ) 
poly.fit( [[2]] )
print( poly.transform( [[2]]) )  # [[2. 4.]]
# 3] 특성 2개인 경우
poly = PolynomialFeatures( include_bias= False)
poly.fit( [[2,3]])               # 특성 (2,3) 규칙(본인값 + 본인제곱값 + 특성들의곱값) / (제곱/곱셈)
print(poly.transform([[2,3]]))   # [[2. 3. 4. 6. 9.]]   # 2,3 / 4,9 / 6
# *] 특성 3개인 경우
poly = PolynomialFeatures( include_bias= False)
poly.fit( [[2,3,4]])
print(poly.transform([[2,3,4]])) # [[ 2.  3.  4.  4.  6.  8.  9. 12. 16.]] 9개
# 수동으로 특성의 제곱항을 만들지 않고 자동(PolynomialFeatures)으로 다항 추가

# 2] 다항 회귀 모델
import pandas as pd
df = pd.read_csv('./day13/Fish.csv')
# 1) 특성과 타깃 구성 
X = df[ ['Length2' , 'Height' , 'Width'] ] # 특성 3개
Y = df['Weight'] # 타깃 1개
# 2) 훈련용/테스트용 분리 8:2
from sklearn.model_selection import train_test_split
X_train , X_test, Y_train , Y_test =  train_test_split( X , Y , test_size=0.2 , random_state=42 )
# 3) 과소적합 해결/방지 하고자 항 추가 == PolynomialFeatures
poly = PolynomialFeatures(include_bias=False)
poly.fit( X_train ) # 학습할 특성들을 규칙(제곱/곱셈) 찾기
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)
print(X_train.shape) # (127,3) 127,3 (특성)
print(X_train_poly.shape) # (127, 9) 127,9(특성-> 항 추가됨 확인)
# 4) 모델 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit( X_train_poly , Y_train ) # 항이 추가된 특성으로 학습  
# 5) 결정 계수
from sklearn.metrics import r2_score
Y_pred = model.predict( X_test_poly ) # 테스트용 다항 특성으로 예측*
print( 'r2 : ' , r2_score(Y_test , Y_pred) ) # r2_score( 정답지 , 예측값 ) 0.9719372415762594

# 3] 다항의 차수 늘리기 , degree = 10 , (차수N) 제곱까지 하여 항 추가하기/생략시 2
poly = PolynomialFeatures( include_bias=False , degree= 10 )
poly.fit(X_train)
X_train_poly2 = poly.transform( X_train )
print( X_train_poly2.shape ) # 차수2 --> 차수10 증가에 따른 (127, 9) -> (127, 285)
X_test_poly2 = poly.transform( X_test )
# 학습 후 결정계수 확인
model = LinearRegression()
model.fit( X_train_poly2 , Y_train ) # 항이 추가된 특성으로 학습
from sklearn.metrics import r2_score
Y_pred = model.predict( X_test_poly2 ) # 테스트용 다항 특성으로 예측
print( 'r2 : ' , r2_score( Y_test , Y_pred)) # r2_score(정답지 , 예측값)
# r2 : 0.07276663213888512
# *] 모델 구현에서 다양한 속성값(degree = N ) 들을 테스트 하여 설계/구현 한다.
# *] 특성이 너무 많아지면 훈련 데이터가 과하게 집학하여 과대적합이 발생하여 점수가 낮아진다.

# 4] 특성이 많아짐에 따라 특성간의 단위 표준화( 0 ~ 1 )
from sklearn.preprocessing import StandardScaler
ss = StandardScaler() # 객체 생성
ss.fit(X_train_poly) # 항이 추가된 특성으로 표준화
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)
print( X_train_poly[0] )
# [ 16.2          4.5924       2.6316     262.44        74.39688
#   42.63192     21.09013776  12.08535984   6.92531856]
print( X_train_scaled[0] )
# [-1.14878727 -1.06273398 -1.10441696 -0.94414637 -1.10959682 -1.06072372
#  -0.91561258 -1.05610367 -1.02825083]
# 평균보다 작으면 음수 

# 5] 규제 : 기울기(가중치) 크기에 페널티를 부여 하여 특성 오차 확인하여 특성 완만/제외
# 1) 릿지
from sklearn.linear_model import Ridge
# 2) alpha(규제강도) : 값이 커질수록 가중치/기울기를 0에 가깝게 규제: 완만
# 반복하여 최적의 규제 강도 찾기
alpha_list = [ 0.001 , 0.01 , 0.1, 1 , 10 , 100 ]
for alpha in alpha_list :
    model = Ridge(alpha= alpha) # 강도 설정하여 릿지 모델 객체 생성
    model.fit( X_train_scaled , Y_train ) # 학습
    # 훈련데이터 점수 와 테스트용 점수 격차 적은 alpha 찾기 
    print( alpha, " : ---훈련용 학습 데이터 점수 vs 테스트용 학습 데이터 점수---")
    print( "Train R2: " , model.score(X_train_scaled , Y_train ) ) 
    print( "Test R2: " , model.score(X_test_scaled , Y_test ) ) # alpha : 10 이 격차가 가장 적다.


 # 3) 라쏘 모델
from sklearn.linear_model import Lasso
lasso = Lasso( alpha=10 ) # 임의의 강도(alpha) 지정 라쏘 모델 객체 생성
lasso.fit( X_train_scaled , Y_train )
print( lasso.score( X_train_scaled , Y_train )) # 0.9587575172401576
print( lasso.score( X_test_scaled , Y_test )) # 0.9609557543588229
# 제거된 특성
import numpy as np
zero_features = np.sum( lasso.coef_ == 0 )
print('기울기가 0으로 제거된 특성 수 :' , zero_features ) # 기울기가 0으로 제거된 특성 수 : 6