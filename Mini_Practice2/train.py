# [종합실습] 의료보험료 예측 모델 - 모델링 파일 (파생변수 버전)
# 데이터셋 : Kaggle Medical Cost Personal Datasets (insurance.csv, 1,338행)
# 목표     : 나이/성별/BMI/자녀수/흡연여부/지역 -> 연간 의료보험료(charges) 회귀 예측
# 결과     : ./Practice_day16/insurance_model.pkl, insurance_metrics.pkl 생성

import pandas as pd
import joblib

# [1] 데이터 로드 및 확인
df = pd.read_csv( "./Mini_Practice2/insurance.csv" )
print( df.head() )
df.info()                       # 1338행, 결측치 없음
print( df.describe() )

# 중복 행 제거 (원본에 완전히 동일한 행이 1개 존재 -> 1338행 -> 1337행)
df = df.drop_duplicates()
print( df.shape )

# [2] 파생변수 생성 : obese_smoker (비만 이면서 흡연자)
# 선형 모델은 각 특성의 효과를 '더하기'만 하므로
# "흡연 + 비만이 동시에 있을 때만 보험료가 급증" 하는 패턴을 표현하지 못한다.
# -> 두 조건을 하나의 특성(0/1)으로 직접 만들어 준다. (day08 mask 방식)
df['obese_smoker'] = 0
df['obese_smoker'] = df['obese_smoker'].mask( ( df['bmi'] >= 30 ) & ( df['smoker'] == 'yes' ), 1 )

# 파생변수 근거 확인 : 흡연여부 x 비만흡연 그룹별 평균 보험료
print( df.groupby( ['smoker', 'obese_smoker'] )['charges'].mean() )
# smoker  obese_smoker
# no      0                8440.66
# yes     0               21363.22
#         1               41557.99   <- 비만+흡연이면 한 번 더 크게 증가 (약 2배)


# [3] 특성(X) / 타깃(Y) 분리
X = df.drop( columns=['charges'] )   # 보험료 제외한 모든 열 (파생변수 포함)
Y = df['charges']                    # 보험료

# [4] 학습용 / 테스트용 분리 (회귀 모델이므로 stratify 사용 안 함)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
print( X_train.shape, X_test.shape )

# [5] ColumnTransformer : 수치형 / 범주형 복합 전처리
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

num_features = ['age', 'bmi', 'children', 'obese_smoker']   # 수치형 (+ 파생변수)
cat_features = ['sex', 'smoker', 'region']                  # 범주형

pp = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features ),
        ('cat', OneHotEncoder( drop='first', sparse_output=False ), cat_features )
    ]
)

# [6] Pipeline + GridSearchCV : LinearRegression / Ridge / Lasso 비교
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import KFold, GridSearchCV

# 모델별 하이퍼파라미터 후보군 (식별자__매개변수명 : [후보값, ...])
# LinearRegression 은 규제가 없어 튜닝할 하이퍼파라미터가 없음 -> 빈 딕셔너리
alpha_list = [0.01, 0.1, 1.0, 10.0, 100.0]
models = [
    { 'name' : 'LinearRegression', 'model' : LinearRegression(),                        'params' : {} },
    { 'name' : 'Ridge',            'model' : Ridge( random_state=42 ),                  'params' : { 'model__alpha' : alpha_list } },
    { 'name' : 'Lasso',            'model' : Lasso( max_iter=10000, random_state=42 ),  'params' : { 'model__alpha' : alpha_list } }
]

# 회귀 모델 교차 검증 분할기 : KFold (5등분)
kf = KFold( n_splits=5, shuffle=True, random_state=42 )

comparison = []     # 모델별 비교 결과 저장 리스트
best_score = -999   # 지금까지 가장 높은 교차검증 R2
best_name = ''      # 가장 좋은 모델 이름
best_grid = ''      # 가장 좋은 그리드서치 결과

for m in models :
    pipe = Pipeline( [ ('pp', pp), ('model', m['model']) ] )
    grid = GridSearchCV( pipe, m['params'], cv=kf, scoring='r2', n_jobs=-1 )
    grid.fit( X_train, Y_train )

    print( m['name'], '최적 파라미터 :', grid.best_params_, '/ 교차검증 R2 :', grid.best_score_ )
    comparison.append( {
        'model_name' : m['name'],
        'best_params' : grid.best_params_,
        'cv_r2' : round( grid.best_score_, 6 )     # 세 모델 차이가 작아 소수 6자리까지 저장
    } )

    # 교차검증 R2 가 가장 높은 모델 기억하기
    if grid.best_score_ > best_score :
        best_score = grid.best_score_
        best_name = m['name']
        best_grid = grid

best_model = best_grid.best_estimator_     # 최적의 추정기(파이프라인 전체)
print( '선택된 모델 :', best_name, best_grid.best_params_ )
# LinearRegression 0.844368 / Ridge 0.844369 / Lasso 0.844432 -> Lasso(alpha=10) 선택

# [7] 테스트(검증) 데이터 기준 성능 평가 : 회귀 모델의 score() == R2
train_r2 = best_model.score( X_train, Y_train )
test_r2 = best_model.score( X_test, Y_test )
print( '학습 R2 :', train_r2 )     # 약 0.8485
print( '테스트 R2 :', test_r2 )    # 약 0.9052
# 테스트 R2 가 학습 R2 보다 높음 -> 과대적합 아님
# (테스트셋 268행이 우연히 예측하기 쉬운 샘플로 구성된 영향, 일반 성능은 교차검증 R2 0.844 가 더 신뢰할 만함)

# [비교용] 파생변수 없이 학습했을 때의 테스트 R2 -> 파생변수 효과 확인
base_pp = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['age', 'bmi', 'children'] ),
        ('cat', OneHotEncoder( drop='first', sparse_output=False ), cat_features )
    ]
)
base_pipe = Pipeline( [ ('pp', base_pp), ('model', LinearRegression()) ] )
base_pipe.fit( X_train.drop( columns=['obese_smoker'] ), Y_train )
base_r2 = base_pipe.score( X_test.drop( columns=['obese_smoker'] ), Y_test )
print( '파생변수 적용 전 R2 :', base_r2, '-> 적용 후 R2 :', test_r2 )   # 약 0.8069 -> 0.9052

# [8] 모델 및 성능 지표 저장 (joblib)
joblib.dump( best_model, './Mini_Practice2/insurance_model.pkl' )

metrics = {
    'model_name' : best_name,                   # 선택된 모델 이름
    'best_params' : best_grid.best_params_,     # 최적 하이퍼파라미터
    'r2' : round( test_r2, 4 ),                 # 테스트 R2 (필수 지표)
    'train_r2' : round( train_r2, 4 ),          # 학습 R2 (과대적합 확인용)
    'base_r2' : round( base_r2, 4 ),            # 파생변수 적용 전 R2
    'comparison' : comparison                   # 3개 모델 교차검증 비교표
}
joblib.dump( metrics, './Mini_Practice2/insurance_metrics.pkl' )
print( '저장 완료 :', metrics )

# [9] 저장된 모델 불러와서 신규 데이터 예측 테스트
loaded_model = joblib.load( './Mini_Practice2/insurance_model.pkl' )

sample = pd.DataFrame( {
    'age' : [30, 30],
    'sex' : ['male', 'male'],
    'bmi' : [32.0, 32.0],
    'children' : [1, 1],
    'smoker' : ['no', 'yes'],
    'region' : ['southeast', 'southeast']
} )
# 예측 시에도 학습 때와 동일하게 파생변수 생성
sample['obese_smoker'] = 0
sample['obese_smoker'] = sample['obese_smoker'].mask( ( sample['bmi'] >= 30 ) & ( sample['smoker'] == 'yes' ), 1 )

print( '비흡연 / 흡연 예측 보험료 :', loaded_model.predict( sample ) )   # 약 [5817.65 38527.43]
