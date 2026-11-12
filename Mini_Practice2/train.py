# [종합실습] 서울시 따릉이 시간당 대여 수요 예측 모델
# 데이터 : Seoul Bike Sharing Demand (UCI / Kaggle, SeoulBikeData.csv)
# 기간 : 2017-12-01 ~ 2018-11-30, 1시간 단위 (8760행)
# 목표 : 날짜/시간/날씨 -> 시간당 따릉이 대여 수(Rented Bike Count) 회귀 예측
# 결과 : ./Mini_Practice2/bike_model.pkl, bike_metrics.pkl 생성

import pandas as pd
import joblib


# [1] 데이터 로드 및 검증
# 1. 데이터 로드
# cp949로 읽으면 컬럼명의 '°' 기호가 깨짐 
# -> latin1 로 읽어야 'Temperature(°C)' 로 제대로 나옴
df = pd.read_csv( "./Mini_Practice2/SeoulBikeData.csv", encoding='latin1' )

# 2. 검증
print( df.head() )
df.info()                       # 8760행(결측치 X)
print( df.describe() )

# 3. 컬럼명 변경 (공백, 특수문자 제거)
df = df.rename( columns={
    'Date' : 'date',
    'Rented Bike Count' : 'count',
    'Hour' : 'hour',
    'Temperature(°C)' : 'temp',
    'Humidity(%)' : 'humidity',
    'Wind speed (m/s)' : 'wind',
    'Visibility (10m)' : 'visibility',
    'Dew point temperature(°C)' : 'dew',
    'Solar Radiation (MJ/m2)' : 'solar',
    'Rainfall(mm)' : 'rainfall',
    'Snowfall (cm)' : 'snowfall',
    'Seasons' : 'season',
    'Holiday' : 'holiday',
    'Functioning Day' : 'functioning'
} )

# 4. 운영 안 한 날 제거 (functioning = 'No' 이면 대여 수 전부 0 -> 예측할 의미 X)
print( df['functioning'].value_counts() )   # Yes 8465 / No 295
df = df[ df['functioning'] == 'Yes' ]
print( df.shape )                           # 8465행 (-295)


# [2] 파생변수 생성
# 1. 날짜 -> 요일 -> 주말 여부
# 날짜가 '01/12/2017' (일/월/연) 형식이라 dayfirst=True 안 넣으면 1월 12일로 읽힘
df['date'] = pd.to_datetime( df['date'], dayfirst=True )
df['weekday'] = df['date'].dt.weekday       # 0(월) ~ 6(일)

df['weekend'] = 0
df['weekend'] = df['weekend'].mask( df['weekday'] >= 5, 1 )   # 토, 일 -> 1

print( df.groupby( 'weekend' )['count'].mean() )
# weekend
# 0    748.11
# 1    682.38    <- 주말이 평일보다 조금 적음

# 2. 비 오는지 여부
df['rain'] = 0
df['rain'] = df['rain'].mask( df['rainfall'] > 0, 1 )

print( df.groupby( 'rain' )['count'].mean() )
# rain
# 0    765.63
# 1    167.26    <- 비 오면 대여 수 1/4 이하로 뚝 떨어짐

# 3. 눈 쌓였는지 여부
# 적설량(snowfall) 숫자만 넣으면 눈 효과가 거의 학습 안 됨 (눈 온 시간이 443행뿐 + 겨울/기온이 효과를 다 가져감)
# -> 비(rain) 처럼 0/1 로 만들어 줌
df['snow'] = 0
df['snow'] = df['snow'].mask( df['snowfall'] > 0, 1 )

print( df.groupby( 'snow' )['count'].mean() )
# snow
# 0    759.19
# 1    185.11    <- 눈 쌓여 있으면 대여 수 1/4 수준

# 4. 시각화 : 평일 / 주말 시간대별 평균 대여 수
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc( 'font' , family = 'Malgun Gothic') # 윈도우 맑은고딕으로 변경 (한글 깨짐 방지)
plt.rcParams['axes.unicode_minus'] = False # 음수 기호 깨짐 방지

# 범례에 0/1 대신 평일/주말로 보이도록 그래프용 컬럼 생성 (학습에는 사용 X)
df['day_type'] = '평일'
df['day_type'] = df['day_type'].mask( df['weekend'] == 1, '주말' )

# ★ 시각화 결과 : 평일은 출근(8시) / 퇴근(18시)에 대여가 확 튀고, 주말은 오후에 완만하게 많음
sns.barplot( data=df, x='hour', y='count', hue='day_type' )
plt.title( '평일 / 주말 시간대별 평균 대여 수' )
plt.xlabel( '시간' )
plt.ylabel( '평균 대여 수' )
plt.legend( title='구분' )      # 범례 제목 day_type -> 구분
plt.show()


# [3] 독립변수(X) / 종속변수(Y) 분리
# 사용 안 하는 열
# dew(이슬점) : 기온 + 습도로 계산되는 값이라 중복
# visibility(가시거리), solar(일사량) : 사용자가 웹에서 입력하기 어려움
# day_type : 그래프 범례용으로 만든 열 (weekend 랑 같은 정보)
X = df.drop( columns=['count', 'date', 'functioning', 'weekday', 'dew', 'visibility', 'solar', 'day_type'] )
Y = df['count']
print( X.columns )      # hour, temp, humidity, wind, rainfall, snowfall, season, holiday, weekend, rain, snow


# [4] 학습용 / 테스트용 분리 (회귀 모델 -> stratify 사용 X)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
print( X_train.shape, X_test.shape )    # (6772, 11) (1693, 11)


# [5] ColumnTransformer : 수치형 / 범주형 복합 전처리
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# ★ hour 는 숫자가 아니라 범주로 사용
# 숫자로 넣으면 "1시간마다 +30대" 같은 직선 하나로만 학습됨
# -> 눈 오는 날에도 밤으로 갈수록 대여 수가 계속 늘어나는 말 안 되는 예측이 나옴
# -> 범주로 넣으면 0시 ~ 23시가 각자 값을 가져서 출퇴근 피크 / 새벽 감소를 표현할 수 있음
num_features = ['temp', 'humidity', 'wind', 'rainfall', 'snowfall', 'weekend', 'rain', 'snow']   # 수치형 (온도, 습도 등 + 파생변수)
cat_features = ['hour', 'season', 'holiday']                                                    # 범주형 : 시간, 계절, 공휴일

pp = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features ),
        ('cat', OneHotEncoder( drop='first', sparse_output=False ), cat_features )
    ]
)


# [6] 파이프라인 + GridSearchCV (LinearRegression / Ridge / Lasso 비교)
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import KFold, GridSearchCV

# 하이퍼파라미터 후보군 (LinearRegression 은 튜닝할 게 없어서 빈 딕셔너리)
alpha_list = [0.01, 0.1, 1.0, 10.0, 100.0]
models = [
    { 'name' : 'LinearRegression', 'model' : LinearRegression(),                        'params' : {} },
    { 'name' : 'Ridge',            'model' : Ridge( random_state=42 ),                  'params' : { 'model__alpha' : alpha_list } },
    { 'name' : 'Lasso',            'model' : Lasso( max_iter=10000, random_state=42 ),  'params' : { 'model__alpha' : alpha_list } }
]

# KFold 분할기 (회귀 -> 일반 KFold)
kf = KFold( n_splits=5, shuffle=True, random_state=42 )

comparison = []     # 모델별 결과 저장
best_score = -999   # 가장 높은 교차검증 R2 (R2는 음수도 나올 수 있어서 아주 작은 값으로 시작)
best_name = ''
best_grid = ''

for m in models :
    pipe = Pipeline( [ ('pp', pp), ('model', m['model']) ] )
    grid = GridSearchCV( pipe, m['params'], cv=kf, scoring='r2', n_jobs=-1 )
    grid.fit( X_train, Y_train )

    print( m['name'], '최적 파라미터 :', grid.best_params_, '/ 교차검증 R2 :', grid.best_score_ )
    comparison.append( {
        'model_name' : m['name'],
        'best_params' : grid.best_params_,
        'cv_r2' : round( grid.best_score_, 6 )   # 세 모델 차이가 작아서 6자리까지
    } )

    # 교차검증 R2 가 제일 높은 모델 저장
    if grid.best_score_ > best_score :
        best_score = grid.best_score_
        best_name = m['name']
        best_grid = grid

best_model = best_grid.best_estimator_
print( '선택된 모델 :', best_name, best_grid.best_params_ )
# LinearRegression 0.678332 / Ridge(alpha=1) 0.678352 / Lasso(alpha=0.1) 0.678337 -> Ridge 선택
# 세 모델 차이 거의 없음 (데이터 8천행에 비해 특성이 적어서 규제 효과가 작음)


# [7] 테스트 데이터로 성능 평가 (회귀 모델 score() == R2)
train_r2 = best_model.score( X_train, Y_train )
test_r2 = best_model.score( X_test, Y_test )
print( '학습 R2 :', train_r2 )     # 0.6829
print( '테스트 R2 :', test_r2 )    # 0.6796 (시간 숫자일 때 0.5663 -> 범주 + 눈 여부로 0.6796)
# 학습 R2 와 테스트 R2 차이 거의 없음 -> 과대적합 X

# 새벽 시간대 등에서 음수 예측이 나옴 -> 서버에서 0 으로 바꿔서 보여줌
Y_pred = best_model.predict( X_test )
print( '음수 예측 개수 :', ( Y_pred < 0 ).sum() )     # 149개


# [8] 모델 + 성능 지표 저장 (joblib)
joblib.dump( best_model, './Mini_Practice2/bike_model.pkl' )

metrics = {
    'model_name' : best_name,                   # 선택된 모델
    'best_params' : best_grid.best_params_,     # 최적 하이퍼파라미터
    'r2' : round( test_r2, 4 ),                 # 테스트 R2 (필수 지표)
    'train_r2' : round( train_r2, 4 ),          # 학습 R2
    'comparison' : comparison                   # 3개 모델 교차검증 비교표
}
joblib.dump( metrics, './Mini_Practice2/bike_metrics.pkl' )
print( '저장 완료 :', metrics )


# [9] 저장한 모델 불러와서 예측 테스트
loaded_model = joblib.load( './Mini_Practice2/bike_model.pkl' )

# 같은 여름 평일 저녁 18시, 맑은 날 vs 비 오는 날
sample = pd.DataFrame( {
    'hour' : [18, 18],
    'temp' : [27.0, 27.0],
    'humidity' : [55, 90],
    'wind' : [2.0, 2.0],
    'rainfall' : [0.0, 5.0],
    'snowfall' : [0.0, 0.0],
    'season' : ['Summer', 'Summer'],
    'holiday' : ['No Holiday', 'No Holiday'],
    'weekend' : [0, 0]
} )
# 예측할 때도 학습 때랑 똑같이 파생변수 만들어줘야 함
sample['rain'] = 0
sample['rain'] = sample['rain'].mask( sample['rainfall'] > 0, 1 )
sample['snow'] = 0
sample['snow'] = sample['snow'].mask( sample['snowfall'] > 0, 1 )

print( '맑은 날 / 비 오는 날 :', loaded_model.predict( sample ) )   # [1913.76 1132.24] -> 비 오면 약 780대 감소
