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

# 매크로(프로그램) -> RPA


