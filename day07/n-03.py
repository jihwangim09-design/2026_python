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

# 2] 병합2 , concatenate( (배열1,배열2) , ) / vstack이랑 결과는 똑같음
z = np.concatenate( (x,y) , axis = 0) # axios = 0 세로방향 / =1 가로방향
print(z) 
