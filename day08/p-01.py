# 판다스 : 데이터 조작 및 분석(표형태) 라이브러리
# 설치 : pip install pandas
# 호출
import pandas as pd
print( pd.__version__)


# 1] 데이터프레임 : 2차원(표) , pd.DataFrame(리스트/딕셔너리)
data_list = [ [ 'ant' , 25 , 'seoul'] , 
    ['bee' , 30 , 'busan'] , 
    ['cat' , 35 , 'incheon'] ] # 2차원 리스트

x = pd.DataFrame( data_list )
print(x) # 행 과 열 => 표 형식
x = pd.DataFrame(data_list , columns=['name' , 'age' , 'city'])
print(x)
x = pd.DataFrame(data_list , index=['a' , 'b' , 'c'])
print(x)

# 2] 데이터프레임2 , pd.DataFrame(딕셔너리) , 키(열이름) 
data_dict = { 
  'name' : ['ant','bee','cat'] , 
  'age' : [25,30,35] , 
  'city' : ['seoul','busan','incheon'] } # 딕셔너리 
df = pd.DataFrame( data_dict )
print(x)

# 3] 특정 컬럼의 값들을 추출 , df['열이름']
ages = df['age'] # 나이 추출
print(ages) # Series(1차원)
print(type(ages)) # <class 'pandas.Series'>
print(type(ages.values)) # <class 'numpy.ndarray'>

# 4] 데이터프레임3 : 넘파이
import numpy as np
data_np = np.array( data_list ) # 넘파이 자료
df = pd.DataFrame( 
    data_np,
    columns= [ 'name' , 'age' , 'city'] ,
    index= ['A' , 'B' , 'C']
    )
print(df)

# 매크로(프로그램) -> RPA(사무 업무 / 파이썬)


# 5] 주요 속성
print( df.shape ) # 행/열 크기 # (3,3)
print( df.columns ) # 컬럼 목록 Index(['name' , 'age' , 'city'], dtype='str')
print( df.index ) # 인덱스 목록 Index(['A' , 'B' , 'C'] , dtype='str')
print( df.values ) # 값만 2차원 리스트로 추출
# [['ant' '25' 'seoul']
# ['bee' '30' 'busan']
# ['cat' '35' 'incheon']]
print( df.head(2)) # 상위 n개 만 반환
# A  ant  25  seoul
# B  bee  30  busan
print( df.tail(2)) # 하위 n개 만 반환
# B  bee  30    busan
# C  cat  35  incheon
df.info() # 컬럼이름 , 결측치, 타입 확인
# <class 'pandas.DataFrame'>
# Index: 3 entries, A to C
# Data columns (total 3 columns):
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
# 0   name    3 non-null      str  
# 1   age     3 non-null      str  
# 2   city    3 non-null      str  
# dtypes: str(3)
# memory usage: 96.0+ bytes

# 6] 인덱싱 = df.iloc[행인덱스, 열인덱스] /슬라이싱
print(df.iloc[1]) # 1행
# memory usage: 96.0+ bytes
# name      bee
# age        30
# city    busan
# Name: B, dtype: str
print(df.iloc[ 1 , 2 ]) # busan
print(df.loc['B']) # 1행 = B행
print(df.loc['B' , 'city']) # B행 city열 # busan

# 7] 슬라이싱 , [시작인덱스:끝인덱스]
print( df.iloc [0:2 , 0:1])
#    name
# A  ant
# B  bee
print( df.loc['A' : 'C' , 'name' : 'age'])
#   name age
# A  ant  25
# B  bee  30
# C  cat  35