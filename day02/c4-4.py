#p.251
numbers = [ 103, 52, 273, 32 , 77 ]
print( min(numbers) ) #min( 리스트 ) 최솟값
print( min(numbers) ) #max( 리스트 ) 최댓값
print( min(numbers) ) #sum( 리스트 ) 합계
#p.252 revered( 리스트 )
numbers_revered = reversed(numbers) # 리스트 뒤집기
print( numbers_revered )
print( next( numbers_revered))
print( list( numbers_revered))
# int( ) float( ) str( ) list( ) : 특정 타입으로 변환 함수

#p.264
# '반복할 수 있는 것'을 프로그래밍 용어로 이터러블(iterable)이라 함
# 이터러블 : 요소들을 하나씩 차례로 꺼내기 가능한 객체 의미
#p.265
# 이터러블 중에서 next()함수를 적용해 하나하나 꺼낼 수 있는 요소를 이터레이터(iterator)
# 이터레이터 : 이터러블 중에서 하나씩 차례로 빼낼 수 있는 요소
# 이터레이터 포함된 타입 : 리스트 / 딕셔너리 / 문자열 / 튜플
# 이터레이터 하나씩 꺼내는 함수 = next( ) 함수 --> 이터러블 
# 즉] 이터레이터가 존재하는 자료만 for 사용가능!


#p.254 enumerate( 리스트 ) , [(인덱스,값)] , (인덱스,값)] 
numbers = [ 103 , 52 , 273 , 32 , 77 ] # <enumerate object at 0x000001679FB75670>
print (enumerate(numbers) ) # [(0, 103), (1, 52), (2, 273), (3, 32), (4, 77)]
print ( list( enumerate( numbers ) ) )  
for index, value in enumerate( numbers ):
    print( index , value )


#p.256 items(딕셔너리) [ (key,value) , (key,value)]
dict_a = { "name" : "유재석" , "age" : 10}
for key , value in dict_a.items():
    print(key ,value)

#p.258 리트스 내포 , 인덱스 자리에 반복문 사용 가능
# 0보다 20까지 2씩 증가한 자료들을 리스트에 저장
# 방법1]
array = []
for i in range(0,21,2):
    array.append(i)
#방법2] 리스트변수 = [ 값 for 반복변수 in range()]
array = [ i for i in range ( 0 , 21 , 2)]
# 활용 : 10 제외한 , 리스트 변수 = [값 for 반복변수 in range() if 조건식 ]
array = [ i for i in range( 0 ,21 , 2) if i != 10 ]

# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]