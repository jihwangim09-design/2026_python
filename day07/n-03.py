import numpy as np # 넘파이 호출
# 1] 병합 , vstack( [배열1,배열2] ) , hstack( [배열1,배열2] )
x = np.array( [ [1,2] , [3,4] ] ) # 2차원 배열
y = np.array( [ [5,6] , [7,8] ] )
z = np.vstack( [x,y] )
print( z ) 
# [[1 2]
# [3 4]
# [5 6]
# [7 8]]
z = np.hstack( [x,y] )
print(z)
# [[1 2 5 6]
# [3 4 7 8]]

# 2] 병합2 , concatenate( (배열1,배열2) , ) # axios = 0 세로방향 / =1 가로방향
z = np.concatenate( (x,y) , axis = 0) # vstack이랑 결과 똑같음 세로방향
print(z) 
z = np.concatenate( (x,y) , axis = 1) # hstack이랑 결과 똑같음 가로방향
print(z)

# 3] 정렬 , np.sort(배열) : 오름차순 , [ : : -1 ] 내림챃순
x = np.array( [3,1,4,2,5] )
print( np.sort(x)) # [1 2 3 4 5]
print( np.sort(x)[ : : -1]) # [5 4 3 2 1]
print(x) # 원본 변경 안됨. # [3 1 4 2 5]
x.sort() # 배열.sort()
print(x) # 원본 자체 변경됨 # [1 2 3 4 5]

scores = np.array( [75,95,60,88] )
z = np.argsort(scores) # 정렬 했을 때 위치순번 반환 (내림차순???) 
print(z) # [2 0 3 1]
print(z[-1]) # 1