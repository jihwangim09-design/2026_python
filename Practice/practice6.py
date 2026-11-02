import pandas as pd
df = pd.read_csv( './Practice/train.csv')


# 1, 가설
# 2. 가설에 따른 자료 수집
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 )
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# 3 : 자료 전처리 
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
df['Age'] = df['Age'].fillna( df['Age'].median())
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.
df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode()[0])
df.info() # 결측데이터확인

# 5-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
#   0 = No(사망자) 1 = Yes(생존자)
import matplotlib.pyplot as plt
import seaborn as sns
# 윈도우 기준 한글 폰트 설정 및 마이너스 부호 깨짐 방지
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
# 시본 기본 테마 적용 (폰트 설정 유지)
sns.set_theme(font='Malgun Gothic', rc={'axes.unicode_minus': False}, style='whitegrid')
# sns.countplot(data='판다스자료' , x = "개수컬럼명" ) # 그룹별개수
sns.countplot( data=df , x="Survived")
plt.show()

# 5-2 : 연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
사망자나이 = ( df[df['Survived'] == 0]['Age']) # 사망자들의 나이만 추출
생존자나이 = ( df[df['Survived'] == 1]['Age']) # 생존자들의 나이만 추출
sns.histplot( data=사망자나이 )
sns.histplot( data=생존자나이 )
plt.legend()
plt.show()

# 5-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot( data=df , x = 'Sex' , hue='Survived')
plt.show()
# 5-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot( data=df , x = 'Pclass' , hue='Survived')
plt.show()
# 5-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot( data=df , x = 'Embarked' , hue='Survived')
plt.show()

# [5. 데이터 시각화 및 분석]





# # 문제2[ 서울시 공공자전거 대여이력 분석]
# 출처: 서울 열린데이터 광장

import pandas as pd
data1 = pd.read_csv('./Practice/서울특별시 공공자전거 대여이력 정보_2501.csv', encoding='cp949')
data2 = pd.read_csv('./Practice/서울특별시 공공자전거 대여이력 정보_2502.csv', encoding='cp949')

# [4. 데이터 전처리 및 병합]
# 4-1 (병합): pd.concat을 사용하여 분리된 월별 데이터를 하나로 통합하고 인덱스를 재부여한다.
df = pd.concat( [data1 , data2] , ignore_index=True )
# 4-2 (정제): 결측치의 문자열 표현('\N')을 None으로 치환하고, 성별 데이터를 대문자로 통일 및 결측치를 'U'로 보정한다.
# df.replace( {"기존값" , "새로운값" , "기존값" , "새로운값"}) # 2개 이상 치환
df = df.replace( {"\\n" : None , "" : None}) # 줄바꿈 과 공백을 None으로 치환
df['성별'] = df['성별'].str.upper().fillna('U')
# 4-3 (형변환): 이용시간, 거리 등 주요 수치형 변수는 pd.to_numeric으로 변환하고, 날짜 데이터는 pd.to_datetime으로 객체화한다.
df['이용시간(분)'] = pd.to_numeric( df['이용시간(분)'] , error = "coerce").fillna(0)
df['이용거리(M)'] = pd.to_numeric( df['이용거리(M)'] , error = "coerce").fillna(0)
df['대여일시'] = pd.to_datetime( df['대여일시'])
df['반납일시'] = pd.to_datetime( df['반납일시'])
# 4-4 (파생변수): 대여일시에서 시간(Hour) 정보를 추출하여 '대여 시간대' 열을 새롭게 생성한다.
df['대여시간대'] = df['대여일시'].dt.hour
df.info()   

# [5. 데이터 시각화 및 분석]
# 5-1 (성별 분포): sns.countplot을 사용하여 성별에 따른 따릉이 이용 비중을 시각화한다.
sns.countplot( data=df , x = '성별')
plt.show()
# 5-2 (시간대 분석): sns.barplot을 사용하여 24시간 중 어느 시간대에 대여가 집중되는지 분석한다.
sns.countplot( data=df , x = '대여 시간대')
plt.show()
# 5-3 (인기 대여소): value_counts().head(10)를 활용하여 가장 활발한 상위 10개 대여소를 가로 막대 그래프로 시각화한다.
인기대여소 = df['대여 대여소명'].value_counts().head(10) # 대여 대여소명 개수추출 후 상위 10개 추출
sns.barplot( x=인기대여소.values ,y=인기대여소.index ) # x = 대여수 , y = 대여명
plt.show()

# 5-4 (상관관계): sns.heatmap을 통해 이용시간, 이용거리, 시간대 등 수치 데이터 간의 밀접도를 분석한다.

수치형자료들 = df.select_dtypes( include='number') # 수치형만 추출
상관관계 = 수치형자료들.corr() # 상관관계 계수 계산 추출
sns.heatmap( 상관관계 , fmt=".2f" , annot=True)
plt.show()