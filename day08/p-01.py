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

# 8] 열 추가 , df[새로운열] = 새로운값
df['score'] = [100 , 80 , 95]
print(df)
#   name age     city  score
# A  ant  25    seoul    100
# B  bee  30    busan     80
# C  cat  35  incheon     95

# 9] 값 수정 , df[수정할열] = 새로운값
df['age'] = [31, 52, 40]
print(df)
#   name  age     city  score
# A  ant   31    seoul    100
# B  bee   52    busan     80
# C  cat   40  incheon     95
df.loc['B' , 'age'] = 70 # B행의age열을 수정
print(df)
#   name  age     city  score
# A  ant   31    seoul    100
# B  bee   70    busan     80
# C  cat   40  incheon     95
df.iloc[0,0] = 'apple'
print(df)
#     name  age     city  score
# A  apple   31    seoul    100
# B    bee   70    busan     80
# C    cat   40  incheon     95

# 10] 여러개 수정 
df.loc[ ['A','B'] , 'score'] = [50,60]
print(df)
#     name  age     city  score
# A  apple   31    seoul     50
# B    bee   70    busan     60
# C    cat   40  incheon     95
# 11] 필터링 조건
print(df['score'] > 70)
# A    False
# B    False
# C     True
print(df[df['score'] > 70]) # 원본에서 조건이 True것만 전체가 나온다 / 조건전체에 [] 로 감싸줘야함 
#   name  age     city  score
# C  cat   40  incheon     95
cont = df['age'] >= 40
print( df[ (df['score'] > 70) & cont] )
#   name  age     city  score
# C  cat   40  incheon     95
print( df[(df['score'] > 70) | cont])
#   name  age     city  score
# B  bee   70    busan     60
# C  cat   40  incheon     95

# 필터링 이용하여 새로운 열
df['passed'] = False
df.loc[ df['score'] > 70 , 'passed'] = True
print(df)
#     name  age     city  score   passed
# A  apple   31    seoul     50    False
# B    bee   70    busan     60    False
# C    cat   40  incheon     95    True

# 12] 컬럼명 변경, df.rename=(columns= {'기존열이름' : '새로운이름'}) 
df = df.rename( columns= {'city' : '도시' , 'age' : '나이'})
print(df)
#    name  나이     도시  score  passed
# A  apple  31    seoul     50   False
# B    bee  70    busan     60   False
# C    cat  40  incheon     95    True

# 13] 집계 , df.describe() , df['열이름'].통계함수()
print( df.describe() )
#              나이     score
# count   3.000000   3.000000
# mean   47.000000  68.333333
# std    20.420578  23.629078
# min    31.000000  50.000000
# 25%    35.500000  55.000000
# 50%    40.000000  60.000000
# 75%    55.000000  77.500000
# max    70.000000  95.000000
print( df['나이'].sum()) # 141
print( df['passed'].value_counts() ) # 자료 빈도 수
# passed
# False    2
# True     1

# 14] 합치기/병합
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})
# 세로 연결 pd.concat( [df1 , df1] , axis = 0 , ignore_index=True)
new_df = pd.concat([df1,df2] , axis=0 , ignore_index=True) # ignore_index=True : 원래 행 번호(인덱스)를 무시하고 0부터 새로 매긴다(기본값은 False)
print(new_df)
#    ID  Score
# 0   1     90
# 1   2     80
# 2   3     85
# 0   4     75
# 1   5     95
# 2   6     88

new_df = pd.concat( [df1,df2] , axis=1)
print(new_df)
#    ID  Score  ID  Score
# 0   1     90   4     75
# 1   2     80   5     95
# 2   3     85   6     88