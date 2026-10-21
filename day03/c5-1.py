# 함수? 코드의 집합
    # 값저장 = 변수 , 실행코드저장 = 함수
    # 값여러개저장 = 리스트/딕셔너리/튜플
# 매개변수란? 함수를 호출할 때는 괄호 내부에 여러 가지를 넣는 변수
# 리턴값? 함수를 호출해서 최종적으로 나오는 결과

# def 함수명( 매개변수명 ) :
#   실행문

# 값 재사용 = 변수 , 코드 재사용 = 반복문(반복패턴존재) / 함수(입력/출력)
# 반복패턴 : 리스트(인덱스)

# 1. 기본적인 함수
def print_3_time( ):    # 함수 정의/
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_time() # 함수 사용/호출
# vs
for i in range( 0 , 3, 1):
    print("안녕하세요")
# 2. 매개변수? 매개(중매-서로 다른 곳에서 연결) , 인수/인자값 -> 매개변수
# 파이썬은 { }가 아닌 탭(들여쓰기) 이용하여 구역 구분
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5) # 인수/인자값 란? 함수 호출할 때 매개변수에 전달하는 값
print_n_times("안녕하세요", 3)
# print_n_times("안녕하세요") # 매개변수는 약속 이고 어기면 실행 안됨

#p.278 가변 매개변수 , p.211 전개연산자
# 조건1: 가변매개변수가 가장 뒤로 정의한다. # 조건2: 1번만 사용
# def 함수명( 매개변수, 매개변수 , *가변매개변수 ):
def print_n_times2(n , *values) :
    for i in range(n):
        for value in values: # [안녕하세요,즐거운,파이썬]
            print( value )
        print()
print_n_times2( 3 , "안녕하세요" , "즐거운" , "파이썬")  #인수4개 , 안녕하세요/즐거운/파이썬 * 3
print_n_times2( 3 , "안녕하세요" , "즐거운")  #인수3개 , 안녕하세요/즐거운 * 2




#p.279 기본 매개변수 , 매개변수에 기본값 대입 형태 , 인수/인자 값 생략 시 적용
def print_n_times3( value , n = 2) :
    for i in range( n ):
        print( value )
print_n_times3( "안녕하세요" )        # "안녕하세요""안녕하세요"
print_n_times3( "안녕하세요" , 3 )    # "안녕하세요""안녕하세요""안녕하세요"

#p.280
# 기본 매개변수가 가변 매개변수보다 앞에 올때 , 오류
# def print_n_times(n=2, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
#
# print_n_times("안녕하세요", "즐거운", "파이썬")

# 가변 매개변수가 기본 매개변수보다 앞에 올때 , 기본 매개변수 인자값 없다.
# # def print_n_times(*values, n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
#
# print_n_times("안녕하세요", "즐거운", "파이썬", 3)

# 해결방안 : 키워드 매개변수
print("안녕하세요") # 안녕하세요 출력 코드
print("안녕하세요" , end = "\n") # end매개변수는 출력 후 무엇을 할지 # \n 기본값 = 기본매개변수
print("안녕하세요" , end = "" ) # 키워드매개변수란? 인수 대입시 매개변수명 지정

#p.283
def print_n_times4( *values , n=2 ):
    # *매개변수 --> 가변매개변수 # 매개변수명 = 기본값 --> 기본매개변수
    for i in range( n ):
        for value in values:
            print(value)
        print()
print_n_times4("안녕하세요" , "즐거운" , "파이썬" , n=3) # 인수 전달시 매개변수명 지정 3번반복
print_n_times4("안녕하세요" , "즐거운" , "파이썬" , 3) # 2번 반복됨 키워드로 지정을 하지 않아서 n을 안붙혔기 때문 10을 넣어도 2번 반복됨

#p.283 여러 함수 호출 형태
# a : 일반 매개변수 (반드시 넣어야 함)
# b, c : 기본 매개변수 (안 넣으면 10, 100 사용)
def test(a, b=10, c=100):
    print(a + b + c)

# 1) 기본 형태 : 순서대로 a=10, b=20, c=30
test(10, 20, 30)            # 60

# 2) 키워드 매개변수로 모두 지정 : 이름을 적어서 넣음
test(a=10, b=100, c=200)    # 310

# 3) 키워드 매개변수로 순서를 바꿔서 지정 : 이름이 있으면 순서 상관없음
test(c=10, a=100, b=200)    # 310

# 4) 일반 + 키워드 섞어서 : a=10(순서대로), b는 생략 → 기본값 10, c=200(이름 지정)
test(10, c=200)             # 220

#p.285 , 리턴 이란? 함수가 종료되면서 반환 되는 값
x = 3
y = 2
z = x + y # 5 # x + y --> def 내가만든공식() : x + y
def myFunc( x , y ):
    return x + y
z = myFunc( x , y )
# 1] 자료 없는 리턴하기 , java void 
def return_test() :
    print("A 위치 입니다.")
    return # 리턴/함수종료/함수끝   #break 반복문탈출/종료
    print("B의 위치입니다.")
return_test() # B위치는 출력안됨

# 2] 자료와 함께 리턴하기
def return_test2():
    return 100      # return 값 생략시 none 반환
value = return_test2()
print(value)

#p.287  범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output
print("0 to 100:" , sum_all(0,100))
print("0 to 1000:" , sum_all(0,1000))
print("50 to 100:" , sum_all(50,100))
print("500 to 1000:" , sum_all(500,1000))

#p.288 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all2(start=0 , end=100, step=1):
    output = 0

    for i in range(start, end + 1, step):
        output += i
    return output
print("A." , sum_all2(0,100,10))
print("B." , sum_all2(end=100))
print("C." , sum_all2(end=100, step=2))

#p.290 2번
def mul(*values):
    output = 1
    for i in values:
        output = output * i
    return output
print(mul(5,7,9,10))