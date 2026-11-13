# 부스팅 앙상블
# 설치 : pip install lightgbm xgboost catboost
url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
import pandas as pd
df = pd.read_csv(url)
# alcohol,sugar,pH,class( 0:레드 / 1:화이트 )
X = df[ ['alcohol', 'sugar' , 'pH']]    # 독립변수
Y = df[ 'class' ]                       # 종속변수 
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y) # 분할

# 3가지 부스팅 앙상블 사용 , XXXClassifier(분류), XXXRegressor(회귀)
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
# 1) 모델 비교
# n_estimators : 부스팅 사용할 트리 개수 기본값 100 , 권장 1000~3000( 최적 모델 탐색 후 중간 종료 )
# learning_rate : 학습률 , 경사하강법 에서 오차 보정 하기 위한 이동 단위 , 기본값 0.1
models = {
    "XGBoost" : XGBClassifier(n_estimators=1000 , learning_rate=0.05),
    "LightGBM" : LGBMClassifier(n_estimators=1000 , learning_rate=0.05)
}