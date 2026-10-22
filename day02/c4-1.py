#p.192
#리스트란? 대괄화[] 엥 자료를 쉼표로 구분하여 여러 자료들으르 저장.
#[요소 , 요소 , 요소] , 요소 = element
# 인덱스란?  리스트 내 요소들이 저장된 순서번호 , 0 번시작

# 
list_a = [237 , 32 , 103 , "문자열" , True, False] # 리스트 선언
print(list_a[ 2 ]) # 103
print(list_a[ 1:3 ]) # 1~2 까지.      32 , 103 출력
list_a[2] = 7 # 요소 값 수정/변경 ***
print(list_a[2]) # 7

# *** 파이썬에서는 인덱싱이 음수로 가능하다. 
print(list_a[-2]) # = True가 나옴. 

print(list_a[3][1]) # 자
# print(list_a[1][1]) # TypeError

list_1 = [1 , 2,  3] # 1차원
list_2 = [[1 , 2] , [3, 4] , [5 , 6]]   # 2차원
list_3 = [[[1, 2] , [3, 4] , [5, 6]]]   # 3차원
print(list_2[1][0]) # 3
# print(list_3[3][1]) # 오류

# p.196 
list_a = [1 , 2,  3]
list_b = [4 , 5,  6]
print(list_a + list_b)  # 리스트 두 개를 붙인다. (리스트 + 리스트 => 연결)
print(list_a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] / 반복연산자로 , 반복된다. 
print( len(list_a))  # 현재 리스트의 길이를 표현. length와 동일. (3) --> 0,1,2 
list_aa = [[1] , [2] , [3]]   # 2차원
print(list_a + list_aa)  # [1, 2, 3, [1], [2], [3]]

# append() --> 요소 끝에 추가.                              / 리스트명.append(요소)
# insert() --> 요소 중 원하는 곳에 삽입.                /  리스트명.insert(위치, 요소)
# extend() --> 한번에 여러 개의 요소를 추가.       /  리스트명.extend([리스트])
list_a.append(4); print(list_a)
list_a.insert(0,5); print(list_a)

# 주의할 점 : 
list_c = [1 ,2]
list_c + [3]                # 방법 1 ] [1 , 2 , 3] 새로운리스트 생성,  list_c 변화 없다 . 
list_c.append(3)        # 방법 2 ] [1 , 2 , 3]  기존 리스트 유지 , list_c 변화 있다 .


#p. 202 요소 삭제하기 , del 리스트명 [인덱스], 리스트명.pop( 인덱스 )
list_a = [ 1, 2, 3, 4, 5 ]
del list_a[1]       # 1번 인덱스 삭제
print( list_a ) # [ 1, 3, 4, 5 ]
list_a.pop( 2 )     # 2번 인덱스 삭제
print( list_a ) # [1, 3, 5] 
del list_a[ 0 : 2 ] # del 키워드 이용한 슬라이싱 삭제
print( list_a ) # [5]
# 리스트명.remove(값)
list_a.remove( 5 ) #(5) 값 삭제
print( list_a ) #[ ]
# 리스트명.clear() 리스트 내부 요소를 모두 제거
list_a.clear()

# p.204 슬라이싱, [ 시작인덱스 : 끝인덱스 : 단계 ]
numbers = [ 1, 2, 3, 4, 5 ,6, 7, 8 ]
numbers[ 0 : 5 : 2] # 0번부터5-1번 까지 2씩 증가하면서 슬라이싱해라
print( numbers[0 : 5 : 2]) # [ 1, 3 ,5 ]
print( numbers[::-1]) # 시작인덱스 생략시 0 , 끝인덱스 생략시 마지막인덱스 , -1은 역순

# p.205 정렬 , 리스트명.sort( ) ,  리스트명.sort(reverse=True) 파괴적으로 동작
list_e = [ 52, 273, 103, 32, 275, 1, 7 ]
list_e.sort()
print( list_e ) # [1, 7, 32, 52, 103, 273, 275]
list_e.sort(reverse=True)
print( list_e ) # [275, 273, 103, 52, 32, 7, 1]

# p.206 내부확인 , 찾을값 in 리스트 / in은 java에서 contains랑 같음
print( 52 in list_e ) # True
print( 51 in list_e ) # False
print( 52 not in list_e ) # True -> False
print( 51 not in list_e ) # False -> True

# p.208 리스트와 반복문 , 리스트내 요소들이 순차적인 인덱스 구조
# for 반복변수 in 반복가능한자료 :                      자바였으면 for( int i = 0 ;  i < list_e.size ; i++ ){ } ... 
#       실행코드

for element in list_e : # vs for( int i = 0 ;  i < list_e.size ; i++ ){ } ... 
    print( element )

for char in "안녕하세요" : # 안녕하세요가 반복되는 이유는 문자열도 리스트/배열임. 문자1개 = 리터럴 리터럴이 모여서 리스트
    print ( char )

# 1. 자바 구구단 작성
# 2. 파이썬 구구단 작성

# 전개연산자 , 리스트명 앞에 * 붙인다.
print( *list_e )

#.213p 1번

list_a = [0,1,2,3,4,5,6,7]

list_a.extend(list_a) # extend() --> 한번에 여러 개의 요소를 추가.
print(list_a)
list_a.append(10)
print(list_a)
list_a.insert(3,0)
print(list_a)
list_a.remove(3)
print(list_a)
list_a.pop(3)
print(list_a)
list_a.clear()
print(list_a)

#.213p 2번

numbers = [273 , 103, 5, 32 , 65, 9, 72, 800, 99 ]

for number in numbers:
    if number > 100 :
        print("- 100 이상의 수: " , number )


#.213p 3번

numbers = [273 , 103 , 5, 32 ,65 , 9 , 72 , 800 ,99]

for number in numbers:
    if number % 2 == 1 :
        print( number,"는 홀수입니다")
    else:
        print( number,"는 짝수입니다")

#for number in numbers:
#   strnum = str(number)
#   print(number,"는",len(strnum),"자릿수입니다.")

#.213p 4번

numbers = [1,2,3,4,5,6,7,8,9]
output = [[] , [] ,[]]

for number in numbers:
    output[number % 3 - 1].append(number)

print(output)

#.213p 5번
numbers = [1,2,3,4,5,6,7,8,9]
for i in range(0, len(numbers) // 2):
    # j가 1, 3, 5, 7이 나오려면
    # 어떤 식을 사용해야 할까요?
    j = (i*2)+1
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2

print(numbers)