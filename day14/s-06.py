# 로지스틱 회귀 : 범주형을 예측하는 대표적인 분류 알고리즘
import pandas as pd
df = pd.read_csv( './day14/Fish.csv')
# 1) 이진 분류 실습 하기 위한 정답지/물고기종류 2가지 사용
df = df[ (df['Species'] == 'Bream')  | (df['Species'] == 'Smelt') ]
X = df[ ['Weight' , 'Length1' , 'Length2' , 'Length3' , 'Height' , 'Width'] ] # 6가지의 특성
Y = df['Species'] # Bream 또는 Smelt
# 2) 분리
# stratify=Y : 무작위 분리한 경우 타깃의 클래스(값) 비율 일정 유지 , 분류모델
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(
    X , Y , test_size=0.2 , random_state=42 , stratify=Y ) 
# 3) 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit( X_train )
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)
# 4) 로지스틱 모델 = 이진(시그모이드) 또는 다중(소프트맥스) 에서 자동 선택 된다.
# L2규제(릿지) : 손실(오차)함수 계산 한다 . C = 1.0 기본값 / 하이퍼파라미터
# 계산반복수(경사하강법) : 최적의 가중치/기울기 찾기 위한 계산 반복수 , 기본값 100 / 권장 1000 ~ 3000
# 경사하강법 : 기울기(가중치) 변경 하면서 최적의 기울기/가중치 찾는 과정
from sklearn.linear_model import LogisticRegression
model = LogisticRegression( C=1.0 , max_iter=1000 , random_state=42)
model.fit( X_train_scaled , Y_train )
Y_pred = model.predict( X_test_scaled )
print( Y_pred ) # ['Bream' 'Bream' 'Smelt' 'Bream' 'Bream' 'Smelt' 'Smelt' 'Bream' 'Bream' 'Bream']
# 5) 결과 속성
print( model.classes_ ) # 정답지 종류 ['Bream' 'Smelt']
print( model.predict_proba(X_test_scaled[ : 3]) ) # 확률 반환
#[[0.99255987 0.00744013] #Bream(0) 열 , Smelt(1)열
# [0.99568698 0.00431302]
# [0.04598467 0.95401533]]
# 6) 정확도 평가 : accuracy_score( 테스트정답지 , 테스트예측 )
from sklearn.metrics import accuracy_score
acc = accuracy_score( Y_test , Y_pred )
print(acc) # 1.0 => 100% 현재 실습은 데이터가 적다.