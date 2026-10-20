# 딕셔너리
#.216p 딕셔너리는 dto json DBrecord랑 호환이 가능해야한다. / java에서 map이랑 비슷함 키 값 구조
#.217p 딕셔너리란? { } 중괄호 선언하고 키:값 형태로 쉼표로 연결
# { key:value , key:value , key:value }
# key중복X / value중복O
# JS:JSON , JAVA:MAP/DTO , DB: RECORD
 
# 1. 선언 , { key:value , key:value }
dict_a = { 'name' : '어벤져스 엔드게임' , 'type' : '히어로 무비'}
# 2. 값호출 , 딕셔너리명['key']
print( dict_a['name']) # 어벤져스 엔드게임
print( dict_a['type']) # 히어로 무비
# 3. 값추가 , 딕셔너리명['새로운 키'] = 새로운값
dict_a[ 'price' ] = 5000
print (dict_a) # {'name': '어벤져스 엔드게임', 'type': '히어로 무비', 'price': 5000}
# 4. 속성값 수정
dict_a['type'] = '호러 무비' # 이미 존재하는 키는 값 수정
print(dict_a)
# 5. 속성 삭제 , del 딕셔너리 ['key']
del dict_a['price'] 
print(dict_a) # {'name': '어벤져스 엔드게임', 'type': '호러 무비'}
# 6. 딕셔너리 내부 'key' 확인 , 찾을키 in 딕셔너리명    // java contains랑 똑같음
print( 'price' in dict_a ) # False
print( 'name' in dict_a ) # True  
# 7. 속성값 호출 , 방법1 : 딕셔너리명['key'] , 방법2 : 딕셔너리명.get( key )
# 차이점 : 방법1은 존재하지 않으면 예외발생, 방법2는 존재하지 않음녀 None 반환
print( dict_a.get('name')) # 어벤져스 엔드게임
print( dict_a.get('price')) # None
# 8. for 반복문 과 딕셔너리 , 딕셔너리내 key 하나씩 for에서 순회
# for key(반복변수) in 딕셔너리명: 여기서 key는 그냥 변수이름임 딕셔너리에서 key를 쓰니까 key가 들어간다는걸 표현
#       실행코드
for key in dict_a: # dict_a의 key를 꺼내서 key에 넣음
    print(dict_a.get(key)) # 방법1      .get(키) -> 그 키의 값을 꺼냄
    print(dict_a[key]) # 방법2         딕셔너리[키] -> 그 키의 값을 꺼냄

#228p 1번
# dict_a = { 'name' : '구름' }
# del dict_a['name']


#228p 2번

pets = [
    {"name" : "구름" , "age" : 5},
    {"name" : "초코" , "age" : 3},
    {"name" : "아지" , "age" : 1},
    {"name" : "호랑이" , "age" : 1}
]
print("# 우리 동네 애완 동물들 ")
for pet in pets:
    age = pet['age']
    strage = str(age)
    print ( pet['name'] + " " + strage+"살")

#228p 3번
numbers = [ 1,3,3,4,5,6,7,7,8,1,4,5,9,6,6,6,7,3,2,1 ]
counter = { }

for number in numbers :
    if number in counter :
        counter[number] += 1
    else :
        counter[number] = 1

print(counter)


#228p 4번
