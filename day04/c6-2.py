# 예외객체란? 발생한 예외 정보 갖는 객체
# 예외클래스 : Exception(예외 최상위클래스)
# except 예외클래스명 as 변수명 :
# as 키워드 : 클래스의 객체변수 생성  
# ValueError, IndexError 대문자인 이유는 클래스라서 e는 변수라서 소문자
# 그외 모든 예외 처리 : 여러개 except 에서 Exception은 항상 마지막에 위치
# 주의할점 : Exception 앞에 위치하면 아래 except 예외가 작동 안함  -> 상속개념
# p.384
list_number = [ 52, 273, 32, 72 , 100 ]
try:
    number_input = int( input('정수입력: ')) # 타입 예외
    print( list_number[ number_input ])     # 인덱스 예외
except Exception as e :               # [1]
    print( e )
except ValueError as e :               # 타입변환 예외
    print( e )
except IndexError as e :               # 인덱스 예외
    print( e )
except IndexError as e :               # 인덱스 예외
    print( e )
