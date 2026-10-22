# p.317 
# 튜플이란? 여러 자료들을 저장하는 리스트와 비슷한 자료형
# 특징: 초기화 이후 수정 불가능
# 사용처: 읽기모드용 VO(Value Object) , 수정없는자료(리스트보다 메모리 효율이 좋다)
# ( 요소,요소,요소 )

# 1. 튜플선언
tuple_test = (10,20,30)
# 2. 요소값 호출
print(tuple_test[0] , tuple_test[2])
# 3. 요소값 수정 , 불가능
# tuple_test[0] = 40 에러나서 주석처리
# 4. 요소 하나인 경우
tuple_test2 = (273,)  # 뒤에 , <- 쉼표가 없으면 일반값 취급
print( tuple_test2 )
# 5. 튜플은 소괄호 생략해도 된다.
( a , b ) = (10 ,20)
print(a , b)
a , b = 10 , 20
print(a , b)
# - 스왑
a , b = b , a # a에 b값 대입 , b에 a값 대입
print( a , b )
# - 리액트(JS)에서 비슷한 문법 존재 -> 구조분해(useState , props)
# name , age = { name : "유재석" , age : 10 }
# name , age = { "유재석" , 10 }
c , d = [ 30, 40 ]
print( c ,d )

# 6. 함수/연산 결과는 항상 1개
def test():
    # return( 10, 20)
    return 10, 20 # 결과는 1개( 10과20묶은 튜풀 )

# 7. 콜백함수 : 함수 그자체를 매개변ㄴ수로 전달하여 전달받은 곳에서 전달받은 함수 호출
#onClick( 회원가입() )[x]--> Oncilck(회원가입)) [o]
def call_10_items( func ): # 값 대신에 함수 받기
    func()
def print_hello():
    print("안녕하세요")

# call_10_items( print_hello() ) # print_hello() 결과값 전달
call_10_items( print_hello ) # print_hello 함수 (그자체)정보 전달

# p.323
# java : 리스트.stream.forEach() , 리스트.stream().map(), 리스트.stream.filter()
# react : 리스트.forEach() , 리스트.map() , 리스트.filter()
# python : for x in 리스트 , map ( 코드 ,리스트 ) , filter( 코드, 리스트 )
# forEach 단순반복(return없다) , map 반복+반환(return있다) , filter 반복+(참이면)반환

def power(item) : 
    return item * item
def under_3(item) :
    return item < 3

list_a = [ 1, 2, 3, 4 , 5]
output_a = map (power , list_a ) # py map
print( output_a )
# JS map : list_a.map( power ) vs list_a.map( x -> return x*x )
output_b = filter ( under_3 , list_a ) # py filter
print( output_b )
# JS filter : list_a.filter(under_3) , list_a.filter( x-> return x < 3 ) 

# p.324 람다(화살표함수)? 코드 줄이기
# lambda 매개변수 : 리턴값    PY : def 함수명():    
# JAVA : () -> { }          JAVA: pubilc void 함수명(){}
# JS : () => { }            JS: function 함수명(){}
power = lambda item : item * item
output_a = map( power , list_a )
# 인라인 람다
#output_a = map( lambda item : item * item , list_a)
# JS1
#const power = (item ) => { return itme*item}
#list_a.map( item => { return power} )
# JS2
#list_a,map( (item) => {return item*item} )

# p.352 1번
numbers = [1, 2, 3, 4, 5, 6]
print("::".join(map(str, numbers)))

# p.352 2번
numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter( lambda x: x % 2 == 1, numbers )))
print()

print("# 3이상 , 7 미만 추출하기")
print(list(filter( lambda x: 3<=x<7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter( lambda x: x * x < 50 , numbers )))
print()
