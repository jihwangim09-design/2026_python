import pandas as pd
fish = pd.read_csv( "./day15/Fish.csv")
# 1) 다중 분류 실습 하기 위한 특성 / 타깃(여러개 어종 ) 구분
X = fish.drop( columns=['Species'])         # 어종 제외한 모든 열
Y = fish['Species']                         # 어종 열
# 2) 분리 , ,stratif=Y 정답지에 학습용과 테스트용 비율 유지(분류 모델 권장)
from sklearn.model_selection import train_test_split
X_trian , X_test, Y_train , Y_test = train_test_split( X ,Y , test_size=0.2 , random_state=42, stratify=Y)
# 3) 다항 특성들의 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_trian) # fit + transfrom
X_test_scaled = ss.transform( X_test)
# 4) 로지스틱 회귀 = 이진 또는 다중에서 자동 선택 된다.
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit( X_train_scaled , Y_train )
Y_pred = model.predict(X_test_scaled)
print( Y_pred[:3]) # ['Bream' 'Perch' 'Smelt']
Y_pred_proba = model.predict_proba( X_test_scaled )
import numpy as np
print( np.round( Y_pred_proba[:3]) , 3 ) # np.round( 리스트 , 자릿수 )
print( model.classes_ ) # 정답지 경우의수 , 타깃의 클래스/값
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']


